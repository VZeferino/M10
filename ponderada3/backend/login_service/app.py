from flask import Flask, jsonify, request, make_response
from flask_restful import Api, Resource
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_swagger_ui import get_swaggerui_blueprint
import logging

logging.basicConfig(filename='user_actions.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

SWAGGER_URL = '/docs'
API_URL = '/static/swagger.yaml'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "List"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Usuarios permitidos
users = {
    "admin@gmail.com": generate_password_hash("admin123")
}

tasks = []

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        logging.info(f'Login successful for user: {username}')
        return username
    logging.warning(f'Failed login attempt for user: {username}')
    return False

@app.route('/login', methods=['POST'])
def login():
    # Extrai o email e a senha da solicitação
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Verifica se o email está no dicionário de usuários e se a senha está correta
    if email in users and check_password_hash(users[email], password):
        logging.info(f'Login successful for user: {email}')
        return jsonify({"message": "Login successful"}), 200
    else:
        logging.warning(f'Failed login attempt for user: {email}')
        return jsonify({"message": "Invalid credentials"}), 401

class UserManagement(Resource):
    def post(self):
        # Adiciona um novo usuário
        data = request.get_json()
        if not data or 'email' not in data or 'password' not in data:
            return make_response(jsonify({"message": "Email e senha são obrigatórios"}), 400)
        
        email = data['email']
        if email in users:
            return make_response(jsonify({"message": "Usuário já existe"}), 400)

        # Gera hash da senha e adiciona ao dicionário de usuários
        users[email] = generate_password_hash(data['password'])
        logging.info(f'New user added: {email}')
        return make_response(jsonify({"message": "Usuário adicionado com sucesso"}), 201)

    def get(self):
        # Retorna todos os usuários cadastrados
        user_emails = list(users.keys())
        return make_response(jsonify({"users": user_emails}), 200)


class TaskList(Resource):
    @auth.login_required
    def get(self):
        # Alterado para usar make_response
        return make_response(jsonify(tasks), 200)

    @auth.login_required
    def post(self):
        data = request.get_json()  # Extrai os dados JSON do corpo da requisição
        if not data or 'title' not in data:
            return make_response(jsonify({"message": "O título da tarefa é obrigatório"}), 400)

        task_id = len(tasks) + 1
        data['id'] = task_id

        # Adiciona a tarefa à lista
        tasks.append(data)

        # Retorna a tarefa criada e um código de status HTTP 201 (Criado)
        return make_response(jsonify(data), 201)
    
class Task(Resource):
    @auth.login_required
    def get(self, task_id):
        task = next((task for task in tasks if task['id'] == task_id), None)
        if task:
            return make_response(jsonify(task), 200)
        else:
            return make_response(jsonify({"message": "Tarefa não encontrada"}), 404)

    @auth.login_required
    def put(self, task_id):
        task = next((task for task in tasks if task['id'] == task_id), None)
        if task:
            data = request.get_json()
            if 'title' in data:
                task['title'] = data['title']
            return make_response(jsonify(task), 200)
        else:
            return make_response(jsonify({"message": "Tarefa não encontrada"}), 404)

    @auth.login_required
    def delete(self, task_id):
        task = next((task for task in tasks if task['id'] == task_id), None)
        if task:
            tasks[:] = [task for task in tasks if task['id'] != task_id]  # Atualizado para evitar usar global
            return make_response(jsonify({"message": "Tarefa deletada"}), 200)
        else:
            return make_response(jsonify({"message": "Tarefa não encontrada"}), 404)

# Adicionando rotas
api.add_resource(UserManagement, '/users')
api.add_resource(TaskList, '/tasks')
api.add_resource(Task, '/tasks/<int:task_id>')

if __name__ == '__main__':
    app.run(debug=True)
