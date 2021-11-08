from django.db import models
from django.urls import reverse


class ModelVehiculo(models.Model):
    kms_recorridos = models.IntegerField()

    class Meta:
        verbose_name = _("modelvehiculo")
        verbose_name_plural = _("modelvehiculos")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("modelvehiculo_detail", kwargs={"pk": self.pk})
