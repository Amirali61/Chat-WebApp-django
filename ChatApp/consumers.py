from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send('{"type":"accept","status":"accepted"}')
        ''' the type in data must be the name of receiver function in consumer '''
        # data = {
        #     "type":"receiver_function",
        #     "message":"Hey there"
        # }

        # print(self.scope.get('session').get('test'))
        # print(self.scope.get('url_route').get('kwargs').get('name'))
        # print(self.channel_layer.groups)
        # print(self.channel_name)
        ''' باید از تابع ایسینک تو سینک استفاده کنیم '''
        async_to_sync(self.channel_layer.group_add)('chat_group',self.channel_name)
        # async_to_sync(self.channel_layer.group_send)('chat_group',data)
    


    def receive(self, text_data):
        # print(json.loads(text_data)["message"])
        print(text_data)
        self.send('"type":"message_arrived","status":"arrived"')

    def disconnect(self, code):
        print(f"the connection closed with code => {code}")

    def receiver_function(self,the_data):
        print(the_data)

