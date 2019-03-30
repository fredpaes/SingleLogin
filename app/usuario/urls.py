from django.urls import path
from .views import *

urlpatterns = [
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('index/', home, name='index'),
    path('cp/', cambio_password, name='c_p'),
]