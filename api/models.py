from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Vehicle(models.Model):
    color = models.CharField(max_length=50)
    identificacion = models.IntegerField()
    kms_recorridos_acumulados = models.FloatField()
    timepo_recorridos_acumulados = models.IntegerField()
    fecha_alta = models.DateField(auto_now=False, auto_now_add=False)
    fecha_baja = models.DateField(auto_now=False, auto_now_add=False)


class Route(models.Model):
    vehiculo = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(auto_now=False, auto_now_add=False)
    fecha_fin = models.DateField(auto_now=False, auto_now_add=False)
    ubicacion_inicio = models.CharField(max_length=50)
    ubicacion_fin = models.CharField(max_length=50)
    fuente_velocidad = models.CharField(max_length=50)
    velocidad_max = models.IntegerField()
    velocidad_media = models.IntegerField()
    velocidad_minima = models.IntegerField()
    kms_recorrido = models.FloatField()
    temperatura_media = models.IntegerField()
    presion_atm_media = models.FloatField()
    viento_predominante = models.CharField(max_length=50)
    nivel_lluvias_media = models.FloatField()
    estado_cota_media = models.FloatField()
    estado_trafico_media = models.CharField(max_length=50)
    calorias_quemadas = models.IntegerField()
    pulsaciones_media = models.IntegerField()
    co2_evitado = models.FloatField()


class Checkpoint(models.Model):
    recorrido = models.ForeignKey(Route, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    ubicacion = models.CharField(max_length=50)
    km_parcial = models.FloatField()
    temperatura = models.IntegerField()
    visibilidad = models.CharField(max_length=50)
    presion_atm = models.FloatField()
    viento = models.FloatField()
    precipitaciones = models.IntegerField()
    radiacion_uv = models.IntegerField()
    nivel_cota = models.FloatField()
    estado_trafico = models.CharField(max_length=50)
    calorias_quemadas = models.IntegerField()
    pulsaciones = models.IntegerField()


class Session(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now=False, auto_now_add=False)
    ingreso = models.BooleanField()
    tipo_dispositivo = models.CharField(max_length=50)
