from rest_framework import serializers
from .models import Usuario
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Usuario
        fields = ['id', 'email', 'nombres', 'apellidos', 'rol', 'num_cel', 'CC']
        read_only_fields = ['fecha_creacion']

    def create(self, validated_data):
        user = Usuario.objects.create_user(**validated_data)
        return user

class ChangePasswordSerializer(serializers.Serializer):
    contraseña_actual = serializers.CharField(required=True)
    nueva_contraseña = serializers.CharField(required=True)

    def validate(self, data):
        usuario = self.context['request'].user
        contraseña_actual = data.get('contraseña_actual')
        nueva_contraseña = data.get('nueva_contraseña')

        if not usuario.check_password(contraseña_actual):
            raise serializers.ValidationError("La contraseña actual es incorrecta.")

        try:
            validate_password(nueva_contraseña, user=usuario)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)

        return data

    def save(self):
        usuario = self.context['request'].user
        nueva_contraseña = self.validated_data['nueva_contraseña']
        usuario.set_password(nueva_contraseña)
        usuario.save()