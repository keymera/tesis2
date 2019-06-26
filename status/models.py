from django.db import models

# Create your models here.


class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    disco = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    procesador = models.CharField(max_length=50)
    bios = models.CharField(max_length=50)
    ipaddress = models.CharField(max_length=50)
    sistema_operativo = models.CharField(max_length=50)
    marca_modelo = models.CharField(max_length=50)
    externo = models.CharField(max_length=50)
    video = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    usuario_equipos = models.CharField(max_length=50)

