from django.apps import AppConfig


class ClothingConfig(AppConfig):
    name = 'clothing'

    def ready(self):
        import clothing.signals
