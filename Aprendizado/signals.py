# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from twilio.rest import Client
from django.contrib.auth import get_user_model
from django.conf import settings
import logging


logger = logging.getLogger(__name__)
User = get_user_model()

@receiver(post_save, sender=User)
def send_sms_on_user_creation(sender, instance, created, **kwargs):
    if created:
        try:
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

            message = client.messages.create(
                to='+5535998232283',  # Substitua pelo número real do destinatário
                from_=settings.TWILIO_PHONE_NUMBER,
                body=f'Novo usuário cadastrado: {instance.username}'
            )
            logger.info(f"SMS enviado para {instance.username}: {message.sid}")
        except Exception as e:
            logger.error(f"Erro ao enviar SMS: {e}")

# signals.py


User = get_user_model()

@receiver(post_save, sender=User)
def send_sms_on_user_creation(sender, instance, created, **kwargs):
    if created:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

        message = client.messages.create(
            to='+5535998232283',  # Substitua pelo número real do destinatário
            from_=settings.TWILIO_PHONE_NUMBER,
            body=f'Novo usuário cadastrado: {instance.username}'
        )
