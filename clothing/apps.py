from django.apps import AppConfig


class ClothingConfig(AppConfig):
    name = 'clothing'

    def ready(self):
        from . import receivers
