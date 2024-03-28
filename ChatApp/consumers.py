from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send('{"type":"accept","status":"accepted"}')

        # print(self.scope.get('session').get('test'))
        print(self.scope.get('url_route').get('kwargs').get('name'))

    def receive(self, text_data):
        # print(json.loads(text_data)["message"])
        print(text_data)
        self.send('"type":"message_arrived","status":"arrived"')

    def disconnect(self, code):
        print(f"the connection closed with code => {code}")

