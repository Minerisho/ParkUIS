from rest_framework import serializers
from .models import Establecimiento, Piso

class EstablecimientoSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Establecimiento
        fields = '__all__'
        
class PisoSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Piso
        fields = '__all__'
    