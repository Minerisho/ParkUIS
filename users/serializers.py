from rest_framework import serializers
from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Usuario
        fields = ['id', 'password', 'email', 'nombres', 'apellidos', 'rol', 'num_cel', 'CC']
        read_only_fields = ['fecha_creacion']

    def create(self, validated_data):
        user = Usuario.objects.create_user(**validated_data)
        return user
