
from rest_framework.response import Response
from .serializers import EstablecimientoSerializer
from .models import Establecimiento
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser


class EstablecimientoVieSet(ModelViewSet):
    queryset = Establecimiento.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = EstablecimientoSerializer
    