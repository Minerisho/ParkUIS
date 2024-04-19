from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UsuarioSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Usuario

from django.shortcuts import get_object_or_404

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def login(request):
    usuario = get_object_or_404(Usuario, email=request.data['email'])
    if not usuario.check_password(request.data['password']):
        return Response({"detail":"Contraseña incorrecta."}, status=status.HTTP_404_NOT_FOUND)
    
    token, created=Token.objects.get_or_create(user = usuario)
    serializer = UsuarioSerializer(instance=usuario)
    return Response({"token":token.key, "usuario": serializer.data})

#--------------------------------Logout--------------------------------
@api_view(['POST'])
def logout(request):
    return Response({})
#--------------------------------Signup--------------------------------
@api_view(['POST'])
def signup(request):
    serializer = UsuarioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        usuario = Usuario.objects.get(email = request.data['email'])
        usuario.set_password(request.data['password'])
        usuario.save()
        token = Token.objects.create(user = usuario)
        return Response({"token":token.key, "usuario": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#--------------------------------test_token--------------------------------
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    
    return Response("Token autenticado correctamente para {}".format(request.usuario.email))
#--------------------------------change_pass--------------------------------
@api_view(['PUT'])
def change_pass(request):
    return Response({})