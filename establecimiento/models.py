from django.db import models

# Create your models here.
class Establecimiento (models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=300)
    
    def __str__(self):
        return self.nombre
    
    
class Piso (models.Model):
    piso = models.IntegerField()
    establecimiento_id = models.ForeignKey(to = Establecimiento, on_delete=models.CASCADE)
    #plazas
    P_motos = models.IntegerField()
    P_carros = models.IntegerField()
    P_bicicletas = models.IntegerField()
    P_emergencias = models.IntegerField()
    P_otros = models.IntegerField()
    P_discapacitados = models.IntegerField()
    
    def __str__(self):
        return f'Piso {self.piso} del establecimiento {self.establecimiento_id.nombre}'
    
