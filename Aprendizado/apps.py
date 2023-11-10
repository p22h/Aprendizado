# apps.py
from django.apps import AppConfig


class SeuAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Aprendizado'

    def ready(self):
        import Aprendizado.signals




class AprendizadoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Aprendizado"


