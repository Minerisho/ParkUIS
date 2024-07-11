from rest_framework import serializers
from .models import Pase


class PaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pase
        fields = '__all__'
        read_only_fields = ['hora_entrada', 'hora_salida', 'usuario_id', 'nombre_vigilante', 'estado', 'temporal']




