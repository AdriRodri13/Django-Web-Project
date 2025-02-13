from django.urls import include, path
from . import views

urlpatterns = [
    path('perfil/', views.perfil, name='perfil'),  
    path('login/', views.login_vista, name='login'),  
    path('signup/', views.signup, name='signup'),  
    path('logout/', views.logout_vista, name='logout'),     
]