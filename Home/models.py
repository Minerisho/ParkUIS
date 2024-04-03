from django.db import models

class ModeloPrueba(models.Model):
    nombre = models.CharField(max_length = 200)
