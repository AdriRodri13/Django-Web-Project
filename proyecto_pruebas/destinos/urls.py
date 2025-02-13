from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.destinos, name='destinos'),
    path('<int:iden>/',views.destino_detalle,name='destino_detalle')
]

