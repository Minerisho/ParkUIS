from rest_framework import serializers
from .models import Vigilante

class VigilanteSerializers(serializers.ModelSerializer):
    class Meta(object):
        model = Vigilante
        fields = '__all__'
        
