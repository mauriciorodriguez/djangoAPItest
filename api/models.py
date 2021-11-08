from django.db import models
from django.urls import reverse


class ModelVehiculo(models.Model):
    kms_recorridos = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("modelvehiculo_detail", kwargs={"pk": self.pk})
