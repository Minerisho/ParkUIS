from django.shortcuts import render
from django.http import HttpResponse
def MensajeHome (request):
    return HttpResponse('<h1> Página Principal <h2>')
