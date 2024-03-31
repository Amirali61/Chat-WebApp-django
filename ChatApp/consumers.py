from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Message , UserChannel
from django.contrib.auth.models import User
import json
from datetime import date,datetime

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send('{"type":"accept","status":"accepted"}')
        user = User.objects.get(id = self.scope.get('url_route').get('kwargs').get('my_id'))
        try:
            user_channel = UserChannel.objects.get(user = self.scope.get('url_route').get('kwargs').get('my_id'))
            user_channel.channel_name = self.channel_name
            user_channel.save()
        except:
            user_channel = UserChannel()
            user_channel.user = user
            user_channel.channel_name = self.channel_name
            user_channel.save()



        
    


    def receive(self, text_data):
        text_data = json.loads(text_data)
        sender_id = self.scope.get('url_route').get('kwargs').get('my_id')
        receiver_id = self.scope.get('url_route').get('kwargs').get('id')
        if text_data.get('type')=='new_message':

            now = datetime.now()


            new_message = Message()
            new_message.from_who = User.objects.get(id = sender_id)
            new_message.to_who = User.objects.get(id = receiver_id)
            new_message.message = text_data.get('message')
            new_message.date = date.today()
            new_message.time = now.time()
            new_message.has_been_seen = False
            new_message.save()


            try:
                user_channel_name = UserChannel.objects.get(user =User.objects.get(id = receiver_id))
                data = {
                    "type":"receiver_function",
                    "type_of_data":"new_message",
                    "data":text_data.get('message')
                }
                async_to_sync(self.channel_layer.send)(user_channel_name.channel_name,data)
            except:
                pass
            
            self.send('"type":"message_arrived","status":"arrived"')
        elif text_data.get("type")=="i_have_seen":
            try:
                user_channel_name = UserChannel.objects.get(user =User.objects.get(id = receiver_id))
                data = {
                    "type":"receiver_function",
                    "type_of_data":"has_been_seen"
                }
                async_to_sync(self.channel_layer.send)(user_channel_name.channel_name,data)

                messages = Message.objects.filter(from_who=User.objects.get(id = receiver_id),to_who=User.objects.get(id = sender_id))
                messages.update(has_been_seen = True)

            except:
                pass


    def disconnect(self, code):
        print(f"the connection closed with code => {code}")

    def receiver_function(self,the_data):
        self.send(json.dumps(the_data))


