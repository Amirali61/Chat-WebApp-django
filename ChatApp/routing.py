from django.urls import path
from . import consumers
ASGI_urlpatterns = [
    path('websocket/',consumers.ChatConsumer.as_asgi()),
    path('websocket/<str:name>',consumers.ChatConsumer.as_asgi())
]