from flask import Flask, request, send_file
from flask_restful import Api, Resource
from PIL import Image
import io

app = Flask(__name__)
api = Api(app)

class ImageProcessing(Resource):
    def post(self):
        if 'image' not in request.files:
            return {"message": "No image provided"}, 400

        image_file = request.files['image']
        image = Image.open(image_file)

        # Exemplo de processamento: converter para preto e branco
        image = image.convert('L')

        # Salvar a imagem processada em um objeto BytesIO
        img_io = io.BytesIO()
        image.save(img_io, 'JPEG')
        img_io.seek(0)

        return send_file(img_io, mimetype='image/jpeg')

api.add_resource(ImageProcessing, '/process')

if __name__ == '__main__':
    app.run(debug=True)
