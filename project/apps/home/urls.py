#Se crea el archivo urls en home, se copio de la urls de config y se borra admin
from django.urls import path
from . import views

#app_name = "home" #se agrega para moverse


urlpatterns = [
    path('', views.index, name="index"),
    path('crear-cliente/', views.crear_cliente, name="crear-cliente"),
    path('crear-alcance1/', views.crear_alcance1, name="crear-alcance1"),
    path('crear-alcance2/', views.crear_alcance2, name="crear-alcance2"),
]
