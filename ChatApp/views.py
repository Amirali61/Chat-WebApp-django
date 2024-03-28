from django.shortcuts import render

# Create your views here.
def home(request):
    # request.session['test']='hi this is me'
    return render(request=request,template_name='chat/home.html')

def login(request):
    return render(request=request,template_name='chat/login.html')

def main(request):
    return render(request=request,template_name='chat/main.html')

def register(request):
    return render(request=request,template_name='chat/register.html')

def chat(request):
    return render(request=request,template_name='chat/chat_person.html')