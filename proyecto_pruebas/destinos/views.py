from django.shortcuts import render,get_object_or_404
from .models import Destino

def destinos(request):
    template_name = 'destinos/destinos.html'
    destinos = Destino.objects.all()
    return render(request, template_name, {"destinos":destinos})

def destino_detalle (request, iden):
    destino = get_object_or_404(Destino, iden = iden)
    return render(request, 'destinos/detalle.html', {"destino":destino})