from django.apps import AppConfig


class AuthAppConfig(AppConfig):
    name = 'authapp'

    def ready(self):
        from . import signals