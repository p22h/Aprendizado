from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail



# Create your views here.

def envia_email (request):
    send_mail('Assunto', 'Email lhe estou enviando', 'phd.importa@gmail.com', ['pauloh222@gmail.com'])
    return HttpResponse('ola')

