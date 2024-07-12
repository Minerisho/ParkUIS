from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import VehiculoSerializer, TipoSerializer
from .models import Vehiculo
from rest_framework import status, generics
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.http import Http404

#---------------ver lista del usuario en sesión--------------
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def ver_mis_vehiculos(request):
    try:
        vehiculos = Vehiculo.objects.filter(usuarioID=request.user.id)
        serializer = VehiculoSerializer(instance=vehiculos, many = True)
        return Response(serializer.data)
    except Http404 as e:
        return Response({"Vehículos no encontrados": str(e)}, status=status.HTTP_404_NOT_FOUND)

#---------------crear vehículo--------------
@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def crear_vehiculo(request):
    datos_vehiculo = request.data
    datos_vehiculo['usuarioID'] = request.user.id
    serializers = VehiculoSerializer(data=datos_vehiculo)
    if serializers.is_valid():
        serializers.save()
        return Response({
            "detail":"Vehículo creado correctamente para el usuario {}".format(request.user.email),
            "vehículo": serializers.data
            }, status=status.HTTP_201_CREATED)
    return Response({"detail": "Ha ocurrido un error en la serialización de datos, osea me enviaste los datos mal, 100% no es mi culpa :v"}, status=status.HTTP_400_BAD_REQUEST)

#---------------Editar vehículo--------------
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def editar_vehiculo(request, pk):

    instance = Vehiculo.objects.filter(usuarioID=request.user.id, pk=pk).first()
    
    if not instance:
        return Response({"error": "Vehículo no encontrado o no tienes permiso para modificar este vehículo."}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = VehiculoSerializer(instance, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    
    return Response({"detail":"vehiculo editado correctamente", "vehiculo":serializer.data}, status=status.HTTP_200_OK)

#---------------Eliminar vehículo--------------
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def eliminar(request, pk = None):
    if not pk:
        return Response({"error":"no proporcionaste la id del vehiculo"}, status=status.HTTP_400_BAD_REQUEST)
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    vehiculo.delete()
    return Response({"detail":"vehiculo eliminado"}, status=status.HTTP_200_OK) 