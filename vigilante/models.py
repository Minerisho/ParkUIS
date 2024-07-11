from django.db import models
from django.utils import timezone
# Create your models here.

class Vigilante (models.Model):
    usuario_id = models.ForeignKey("users.Usuario", on_delete=models.CASCADE)
    establecimiento_id = models.ForeignKey("establecimiento.Establecimiento", null=True, on_delete=models.SET_NULL)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.usuario_id.nombres} {self.usuario_id.apellidos}'

