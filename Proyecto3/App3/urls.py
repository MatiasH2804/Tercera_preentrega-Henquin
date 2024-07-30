from App3 import views
from django.urls import path 

urlpatterns = [
    path('', views.inicio, name= "Inicio"),
    path('club/', views.club, name= "Club"),
    path('jugador/', views.jugador, name= "Jugador"),
    path('dorsal/', views.dorsal, name= "Dorsal"),
    path('buscar-jugador', views.buscar_jugador, name="Buscar-jugador"),

]
