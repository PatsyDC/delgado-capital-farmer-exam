from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class CotizacionCliente(models.Model):
    nombre = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)
    tipoServicio = models.CharField(max_length=255)
    descripcionCaso = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = ('Cliente')

class Cotizacion(models.Model):
    cotizacion_id = models.CharField(max_length=20, unique=True)
    cliente = models.ForeignKey('CotizacionCliente', on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = ('Cotizaciones')

    def _str_(self):
        return self.cotizacion_id