from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

# Create your views here.
def log_in(request):
    if request.method is 'POST':
        # autenticación
        u_name = request.POST.get('username')
        u_pass = request.POST.get('password')
        user = authenticate(request, username=u_name, password=u_pass)
        if user is None:
            # el usuario esta mal
            pass
        elif user.is_active:
            # login
            login(request, user)
            return redirect('index')
        else:
            # el usuario no esta activo
            pass
    else:
        return render(request, 'usuario/login.html')

def log_out(request):
    pass

def cambio_password(request):
    pass

def home(request):
    return render(request, 'usuario/index.html')