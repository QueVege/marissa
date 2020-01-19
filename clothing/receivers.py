from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from django.dispatch import receiver
from .signals import *

@receiver(products_added)
def restart_page(sender, **kwargs):
    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        'viewers',
        {'type': 'restart.message', 'text': 'Restart it!'},
    )