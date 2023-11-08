from django.urls import path, include
from . import views

urlpatterns = [
    path('' , views.envia_email, name = 'envia_mail'),

]