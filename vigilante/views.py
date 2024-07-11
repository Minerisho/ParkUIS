from django.shortcuts import render
from .models import Vigilante
from .serializers import VigilanteSerializers
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response

class VigilanteViewSet(viewsets.ModelViewSet):
    queryset = Vigilante.objects.all()
    serializer_class = VigilanteSerializers
    permission_classes = [IsAdminUser]
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def es_vigilante(request):
    flag = Vigilante.objects.filter(usuario_id=request.user.id, activo=True).exists()
    return Response(flag)