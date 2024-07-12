from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UsuarioSerializer, ChangePasswordSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Usuario
from vehiculos.models import Vehiculo
from vehiculos.serializers import VehiculoSerializer
from django.shortcuts import get_object_or_404

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from vigilante.permissions import IsVigilante


#--------------------------------Login--------------------------------
@api_view(['POST'])
def login(request):
    usuario = get_object_or_404(Usuario, email=request.data['email'])
    if not usuario.check_password(request.data['password']):
        return Response({"detail":"Contraseña incorrecta."}, status=status.HTTP_404_NOT_FOUND)
    
    token, __ = Token.objects.get_or_create(user = usuario)
    serializer = UsuarioSerializer(instance=usuario)
    return Response({"token":token.key, "usuario": serializer.data})

#--------------------------------Logout--------------------------------

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def logout(request):
    request.user.auth_token.delete()
    return Response({"detail": "Sesión cerrada correctamente."})
#--------------------------------Signup--------------------------------
@api_view(['POST'])
def signup(request):
    serializer = UsuarioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        usuario = Usuario.objects.get(email = request.data['email'])
        usuario.set_password(request.data['password'])
        usuario.save()
        return Response({ "usuario": serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#--------------------------------change_pass--------------------------------
@api_view(['PATCH'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def change_pass(request):
    serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response({"detail": "Se ha cambiado la contraseña correctamente."})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#--------------------------------ver_vehiculos--------------------------------
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated, IsVigilante])
def ver_vehiculos(request, pk=None):
    if pk is None:
        return Response({'error': 'No se recibió ningún id en la url.'}, status=status.HTTP_400_BAD_REQUEST)
    
    lista_vehiculos = Vehiculo.objects.filter(usuarioID = pk)
    if not lista_vehiculos.exists():
        return Response({'error': 'No se encontraron vehículos para el id del usuario proporcionado.'}, status=status.HTTP_404_NOT_FOUND)
    
    vehiculos_serializados = VehiculoSerializer(lista_vehiculos, many=True)
    return Response(vehiculos_serializados.data, status=status.HTTP_200_OK)
