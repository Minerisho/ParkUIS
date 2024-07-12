from django.db import models

class Pase(models.Model):
    
    hora_entrada = models.DateTimeField(("hora de entrada"), default=None, null=True, blank= True)
    hora_salida = models.DateTimeField(("hora de salida"), default=None, null=True, blank= True)
    usuario_id = models.IntegerField(null=True)
    json_vehiculo = models.JSONField("información del vehiculo a utilizar", default=dict, null=True, blank= True)
    nombre_vigilante = models.CharField(verbose_name="nombre del vigilante", max_length=50, null = True, blank= True, default=None)
    estado = models.IntegerField(choices=[(0, "sin usar"), (1, "en uso"), (2, "completado"), (3, "perdido")], default=0)
    temporal = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("Pase")
        verbose_name_plural = ("Pases")

    def __str__(self):
        placa = self.json_vehiculo.get('placa', 'Sin placa')
        return f"Pase {self.id} - {self.estado} - {placa}"

    


