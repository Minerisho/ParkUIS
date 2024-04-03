from django.shortcuts import render
from django.http import HttpResponse

def MensajeInicioSesion (request):
    return HttpResponse('Aquí se inicia sesión')