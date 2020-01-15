from django.urls import re_path
from .consumers import MarissaConsumer

websocket_urlpatterns = [
    re_path(r'ws/products/$', MarissaConsumer),
]
