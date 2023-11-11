from django.apps import AppConfig


class AprendizadoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Aprendizado"

    def ready(self):
        import Aprendizado.signals

