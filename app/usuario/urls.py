from django.urls import path
from .views import log_in, home

urlpatterns = [
    path('login/', log_in, name='login'),
    path('index/', home, name='index'),
]