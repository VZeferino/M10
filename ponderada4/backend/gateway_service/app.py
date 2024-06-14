from flask import Flask, jsonify, request, redirect, url_for
from flask_restful import Api, Resource
import logging
import requests

logging.basicConfig(filename='gateway.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

app = Flask(__name__)
api = Api(app)

EVENT_SERVICE_URL = 'http://localhost:5002/events'

class Gateway(Resource):
    def get(self):
        logging.info('Gateway accessed')
        return jsonify({"message": "Gateway is up and running"})

class EventProxy(Resource):
    def get(self, event_id=None):
        if event_id:
            response = requests.get(f'{EVENT_SERVICE_URL}/{event_id}')
        else:
            response = requests.get(EVENT_SERVICE_URL)
        logging.info(f'Request forwarded to Event service: GET /events{"/" + str(event_id) if event_id else ""}')
        return jsonify(response.json()), response.status_code

    def post(self):
        response = requests.post(EVENT_SERVICE_URL, json=request.get_json())
        logging.info('Request forwarded to Event service: POST /events')
        return jsonify(response.json()), response.status_code

    def put(self, event_id):
        response = requests.put(f'{EVENT_SERVICE_URL}/{event_id}', json=request.get_json())
        logging.info(f'Request forwarded to Event service: PUT /events/{event_id}')
        return jsonify(response.json()), response.status_code

    def delete(self, event_id):
        response = requests.delete(f'{EVENT_SERVICE_URL}/{event_id}')
        logging.info(f'Request forwarded to Event service: DELETE /events/{event_id}')
        return jsonify(response.json()), response.status_code

api.add_resource(Gateway, '/gateway')
api.add_resource(EventProxy, '/events', '/events/<int:event_id>')

if __name__ == '__main__':
    app.run(port=5001, debug=True)
