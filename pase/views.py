from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from .models import Pase
from vehiculos.models import Vehiculo
from users.models import Usuario
from vigilante.models import Vigilante
from .serializers import PaseSerializer
from rest_framework.decorators import action, api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from django.utils import timezone
from rest_framework import status
from vigilante.permissions import IsVigilante
import logging

logger = logging.getLogger(__name__)

class PaseViewSet(viewsets.ModelViewSet):
    queryset = Pase.objects.all()
    serializer_class = PaseSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        req_usuario_id = request.user.id

        if Vigilante.objects.filter(usuario_id = req_usuario_id).exists(): #Si el que hace la petición es un Vigilante... está creando un pase temporal
            vigilante_data = request.user
            apellidos= vigilante_data.apellidos
            nombres = vigilante_data.nombres
            json_vehiculo = request.data.get('json_vehiculo')  
            if json_vehiculo is None:
                return Response({'error': 'JSON de vehículo no proporcionado'}, status=status.HTTP_400_BAD_REQUEST)     
                                                                                                                                             
            pase_data={
                "usuario_id":None,
                "json_vehiculo": json_vehiculo,
                "nombre_vigilante": f"{nombres} {apellidos}",
                "hora_entrada": timezone.now(),
                "estado":1,
                "temporal":True
            }
            pase_creado = Pase.objects.create(**pase_data)
            return Response({'id': pase_creado.pk}, status=status.HTTP_201_CREATED)

        else:
            
            pase_creado = Pase.objects.create(usuario_id = req_usuario_id) #Si lo crea un usuario, es un pase normal vacío
            return Response({'id': pase_creado.pk}, status=status.HTTP_201_CREATED)
        

    @action(detail=True, methods=['PATCH'], permission_classes = [IsVigilante])
    def scan(self, request, pk=None):
        pase = self.get_object()
        logger.debug(f"Estado actual del pase: {pase.estado}")
        if pase.estado == 0: #Sin usar | Me envía el json del carro
            pase.json_vehiculo = request.data.get('json_vehiculo')
            if pase.json_vehiculo is None:
                return Response({'error': 'JSON de vehículo no proporcionado'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
            vigilante_data = request.user
            apellidos= vigilante_data.apellidos
            nombres = vigilante_data.nombres
            pase.nombre_vigilante = f'{nombres} {apellidos}'
            logger.debug(f"Fecha de entrada antes del registro: {pase.hora_entrada}")           
            pase.hora_entrada = timezone.now()
            logger.debug(f"Fecha de entrada antes del registro: {pase.hora_entrada}")
            pase.estado = 1
            pase.save()
            return Response({'status': 'Pase establecido en uso', 'id':pase.pk, 'estado':pase.estado}, status=status.HTTP_200_OK)
        elif pase.estado == 1: #En uso
            pase.hora_salida = timezone.now()            
            pase.estado = 2
            pase.save()
            return Response({'status': 'Pase completado', 'id':pase.pk, 'estado':pase.estado}, status=status.HTTP_200_OK)
        elif pase.estado == 2: #Completado
            return Response({'error': 'El pase ya fue completado', 'id':pase.pk, 'estado':pase.estado}, status=status.HTTP_400_BAD_REQUEST)
        elif pase.estado == 3: #Perdido
            return Response({'error': 'El pase está considerado como perdido y nunca fue completado', 'id':pase.pk, 'estado':pase.estado}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'El pase tiene un estado inválido', 'id_pase':pase.pk, 'estado':pase.estado}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['PATCH'], permission_classes = [IsVigilante])
    def perdido(self, request, pk=None):
        pase = self.get_object()
        pase.estado = 3
        pase.save()
        return Response({'status': 'Pase marcado como perdido', 'id':pase.pk}, status=status.HTTP_200_OK)


        
        
    


