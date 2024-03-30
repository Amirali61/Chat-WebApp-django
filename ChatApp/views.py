from django.shortcuts import render ,redirect
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.contrib.auth import login as signin 
from django.contrib.auth import authenticate 
from django.contrib.auth import logout as signout 
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Message
from .forms import RegistrationForm , LoginForm
# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('main')
    else:
        me = request.user
        users = User.objects.all().order_by('username')
        return render(request=request,template_name='chat/home.html',context={'me':me,'users':users})

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request=request,template_name='chat/login.html',context={'form':form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                signin(request, user)
                return redirect('home')
        return render(request,'chat/login.html',{'form': form,'error':'Wrong credentials'})
    
def logout(request):
    signout(request)
    return redirect('login')    

def main(request):
    return render(request=request,template_name='chat/main.html')

def register(request):
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, template_name='chat/register.html', context={'form':form})
    elif request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            signin(request, user)
            return redirect('home')
        else:
            return render(request, 'chat/register.html', {'form': form})


def chat(request , id):
    if not request.user.is_authenticated:
        return redirect('main')
    else:
        person = User.objects.get(id = id)
        me = request.user
        messages = Message.objects.filter(Q(from_who=person,to_who=me)|Q(from_who=me,to_who=person)).order_by('date','time')
        return render(request=request,template_name='chat/chat_person.html',context={'person':person,'me':me,'messages':messages})