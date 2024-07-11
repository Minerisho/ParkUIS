from django.db import models
from users.models import Usuario

class TipoVehiculo(models.Model):
    nombre = models.CharField(primary_key=True, max_length=100)

class Vehiculo(models.Model):
    tipo_vehiculo = models.ForeignKey(to=TipoVehiculo, on_delete=models.SET_NULL, null=True)
    marca = models.CharField(max_length=100, blank=True)
    modelo = models.CharField(max_length=200, blank=True)
    color = models.CharField(max_length=100)
    placa = models.CharField(max_length=20)
    usuarioID = models.ForeignKey(to=Usuario, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'
        
    def __str__(self):
        return f"{self.marca} - {self.modelo} - {self.placa}"