
# consumers.py
from channels.generic.websocket import WebsocketConsumer
import json


class BaseConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass
        # self.send(text_data=json.dumps({
        #     'message': 'ok than'
        # }))

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))
