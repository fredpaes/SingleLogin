from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def log_in(request):
    if request.method == 'POST':
        # autenticación
        u_name = request.POST['username']
        u_pass = request.POST['password']
        user = authenticate(username=u_name, password=u_pass)
        if user is None:
            messages.error(request, ('Error en los credenciales.'))
        elif user.is_active:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, ('El usuario no se encuentra activo.'))
        return render(request, 'usuario/login.html')
    else:
        return render(request, 'usuario/login.html')

def log_out(request):
    logout(request)
    return redirect('login')

def cambio_password(request):
    return render(request, 'usuario/cambiar_password.html')

def home(request):
    return render(request, 'usuario/index.html')