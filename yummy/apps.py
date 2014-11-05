from django.apps import AppConfig as BaseAppConfig
from django.utils.importlib import import_module


class AppConfig(BaseAppConfig):

    name = "yummy"

    def ready(self):
        import_module("yummy.receivers")
