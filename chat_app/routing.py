from django.urls import re_path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    # re_path("ws/chat/(?P<room_name>\w+)/$", ChatConsumer),
    re_path("ws/socket-server", ChatConsumer.as_asgi()),
]