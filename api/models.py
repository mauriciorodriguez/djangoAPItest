from django.db import models


class ModelVehiculo(models.Model):
    kms_recorridos = models.IntegerField()
