from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import logging

logging.basicConfig(filename='events.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

app = Flask(__name__)
api = Api(app)

events = []

class Event(Resource):
    def get(self, event_id):
        event = next((event for event in events if event['id'] == event_id), None)
        if event:
            logging.info(f'Event retrieved: {event_id}')
            return jsonify(event)
        else:
            logging.warning(f'Event not found: {event_id}')
            return jsonify({"message": "Event not found"}), 404

    def post(self):
        data = request.get_json()
        if not data or 'name' not in data:
            return jsonify({"message": "Event name is required"}), 400

        event_id = len(events) + 1
        event = {"id": event_id, "name": data['name']}
        events.append(event)
        logging.info(f'Event created: {event}')
        return jsonify(event), 201

    def put(self, event_id):
        event = next((event for event in events if event['id'] == event_id), None)
        if event:
            data = request.get_json()
            event['name'] = data.get('name', event['name'])
            logging.info(f'Event updated: {event}')
            return jsonify(event)
        else:
            logging.warning(f'Event not found: {event_id}')
            return jsonify({"message": "Event not found"}), 404

    def delete(self, event_id):
        global events
        event = next((event for event in events if event['id'] == event_id), None)
        if event:
            events = [e for e in events if e['id'] != event_id]
            logging.info(f'Event deleted: {event_id}')
            return jsonify({"message": "Event deleted"}), 200
        else:
            logging.warning(f'Event not found: {event_id}')
            return jsonify({"message": "Event not found"}), 404

api.add_resource(Event, '/events/<int:event_id>')

if __name__ == '__main__':
    app.run(port=5002, debug=True)
