from django.db import models

# Create your models here.
class Jugador(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)


class Dorsal(models.Model):
    dorsal = models.IntegerField()

class Club(models.Model):
     equipo = models.CharField(max_length=40) 

# Corre las migraciones



