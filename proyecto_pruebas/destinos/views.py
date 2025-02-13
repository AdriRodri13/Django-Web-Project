from django.shortcuts import render
from .models import Destino

def destinos(request):
    template_name = 'destinos/destinos.html'
    destinos = Destino.objects.all()
    return render(request, template_name, {"destinos":destinos})