from flask import Flask, jsonify, request, make_response
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

pedidos = []

class PedidoList(Resource):
    def post(self):
        data = request.get_json()  # Extrai os dados JSON do corpo da requisição
        if not data or 'pedido' not in data:
            return make_response(jsonify({"message": "O pedido é obrigatório"}), 400)

        pedido_id = len(pedidos) + 1
        data['id'] = pedido_id

        # Adiciona o pedido à lista
        pedidos.append(data)

        # Retorna o pedido criada e um código de status HTTP 201 (Criado)
        return make_response(jsonify(data['id']), 201)
    
class PedidoListGet(Resource):
    def get(self):
        return make_response(jsonify(pedidos), 200)

class Pedido(Resource):
    def get(self, pedido_id):
        pedido = next((pedido for pedido in pedidos if pedido['id'] == pedido_id), None)
        if pedido:
            return make_response(jsonify(pedido), 200)
        else:
            return make_response(jsonify({"message": "Pedido não encontrado"}), 404)

    def put(self, pedido_id):
        pedido = next((pedido for pedido in pedidos if pedido['id'] == pedido_id), None)
        if pedido:
            data = request.get_json()
            if 'pedido' in data:
                pedido['pedido'] = data['pedido']
            return make_response(jsonify(pedido), 200)
        else:
            return make_response(jsonify({"message": "Pedido não encontrado"}), 404)

    def delete(self, pedido_id):
        pedido = next((pedido for pedido in pedidos if pedido['id'] == pedido_id), None)
        if pedido:
            pedidos[:] = [pedido for pedido in pedidos if pedido['id'] != pedido_id]  # Atualizado para evitar usar global
            return make_response(jsonify({"message": "Pedido deletado"}), 200)
        else:
            return make_response(jsonify({"message": "Pedido não encontrado"}), 404)

# Adicionando rotas
api.add_resource(PedidoList, '/novo')
api.add_resource(PedidoListGet, '/pedidos')
api.add_resource(Pedido, '/pedidos/<int:pedido_id>')

if __name__ == '__main__':
    app.run(debug=True)
