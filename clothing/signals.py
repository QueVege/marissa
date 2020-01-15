from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .models import Product


@receiver(post_save, sender=Product)
@receiver(post_delete, sender=Product)
def update_catalog(instance, **kwargs):
    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        'viewers',
        {'type': 'restart.message', 'text': 'Restart it!'},
    )
