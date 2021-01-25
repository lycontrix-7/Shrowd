from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/(?P<server_name>\w+)/$', consumers.ServerConsumer.as_asgi()),
]