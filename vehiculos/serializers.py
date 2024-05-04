from rest_framework import serializers
from .models import Vehiculo, TipoVehiculo


class VehiculoSerializer(serializers.ModelSerializer):
    marca = serializers.CharField(required=False)
    modelo = serializers.CharField(required=False)
    class Meta(object):
        model = Vehiculo
        fields = ['id', 'tipo_vehiculo', 'marca', 'modelo', 'color', 'placa', 'usuarioID']
        read_only_fields = ['fecha_creacion']


class TipoSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = TipoVehiculo
        fields = ['nombre']
       