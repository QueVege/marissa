from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json


class MarissaConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            'viewers',
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            'viewers',
            self.channel_name
        )

    def restart_message(self, event):
        message = event['text']
        self.send(text_data=json.dumps({
            'message': message
        }))
