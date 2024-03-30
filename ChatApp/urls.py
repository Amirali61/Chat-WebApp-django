from . import views 
from django.urls import path

urlpatterns = [
    path('home/',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('register/',views.register,name='register'),
    path('main/',views.main,name='main'),
    path('chat/<int:id>',views.chat,name='chat')
]