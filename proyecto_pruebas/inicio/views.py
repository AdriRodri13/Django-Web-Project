from django.shortcuts import render
from destinos.models import Destino

# Create your views here.
def home(request):
    destinos = Destino.objects.all()[:3]
    return render(request, "inicio/home.html", {"destinos":destinos})
