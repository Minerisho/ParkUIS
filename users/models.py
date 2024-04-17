from django.db import models

class Rol(models.Model):
    nombre_rol = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre_rol

class Usuario(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    rol = models.ForeignKey(to=Rol, on_delete=models.CASCADE)
    email = models.EmailField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=False, editable=False)
    
    def __str__(self):
        return f'{self.id} - {self.username} - {self.rol.nombre_rol}'

class Persona(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.PROTECT,primary_key=True,)
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    CC = models.BigIntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.id} - {self.nombres} {self.apellidos}'
    
