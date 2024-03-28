from django.shortcuts import render
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Create your views here.
def home(request):
    # request.session['test']='hi this is me'

    data = {
            "type":"receiver_function",
            "message":"Hey there"
        }
    
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)('chat_group',data)

    return render(request=request,template_name='chat/home.html')

def login(request):
    return render(request=request,template_name='chat/login.html')

def main(request):
    return render(request=request,template_name='chat/main.html')

def register(request):
    return render(request=request,template_name='chat/register.html')

def chat(request):
    return render(request=request,template_name='chat/chat_person.html')