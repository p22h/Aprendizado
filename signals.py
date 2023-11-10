# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from twilio.rest import Client
from django.contrib.auth.models import User
from django.conf import settings

@receiver(post_save, sender=User)
def send_sms_on_user_creation(sender, instance, created, **kwargs):
    if created:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

        message = client.messages.create(
            to='+5535998232283',  # Substitua pelo número real do destinatário
            from_=settings.TWILIO_PHONE_NUMBER,
            body=f'Novo usuário cadastrado: {instance.username}'
        )
