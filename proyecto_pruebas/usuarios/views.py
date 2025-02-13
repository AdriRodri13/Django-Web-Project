from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.
# Vista de perfil (requiere autenticación)
@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html')

# Vista para iniciar sesión
def login_vista(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Inicio')  # Redirige a la página de inicio después del login
    else:
        form = AuthenticationForm()
    
    return render(request, 'usuarios/login.html', {'form': form})


# Vista para registrarse
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Tu cuenta ha sido creada exitosamente')
            return redirect('login')
        else:
            messages.error(request,'Por favor corrige los errores del formulario')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/signup.html', {'form':form})

# Vista para cerrar sesión
def logout_vista(request):
    logout(request)
    return redirect('Inicio')