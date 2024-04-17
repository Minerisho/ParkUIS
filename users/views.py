from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UsuarioSerializer
from .models import Usuario
from rest_framework import status


@api_view(['POST'])
def login(request):
    return Response({})

@api_view(['POST'])
def logout(request):
    return Response({})

@api_view(['POST'])
def signup(request):
    return Response({})

@api_view(['GET'])
def test_token(request):
    return Response({})

@api_view(['PUT'])
def change_pass(request):
    return Response({})