#Se crea el archivo urls en home, se copio de la urls de config y se borra admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
]
