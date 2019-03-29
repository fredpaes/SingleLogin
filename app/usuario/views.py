from django.shortcuts import render

# Create your views here.
def log_in(request):
    return render(request, 'usuario/login.html')

def log_out(request):
    pass

def cambio_password(request):
    pass