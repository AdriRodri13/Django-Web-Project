from django.shortcuts import render

def destinos(request):
    template_name = 'destinos/destinos.html'  # Asegúrate de que esta ruta es correcta
    return render(request, template_name)