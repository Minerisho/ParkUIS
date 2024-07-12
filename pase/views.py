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
from vehiculos.serializers import VehiculoSerializer

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
                "temporal":True,
                "cc": None
            }
            pase_creado = Pase.objects.create(**pase_data)
            return Response({'id': pase_creado.pk}, status=status.HTTP_201_CREATED)

        else:
            
            pase_creado = Pase.objects.create(usuario_id = req_usuario_id) #Si lo crea un usuario, es un pase normal vacío
            return Response({'id': pase_creado.pk}, status=status.HTTP_201_CREATED)
        

    @action(detail=True, methods=['PATCH'], permission_classes = [IsVigilante])
    def scan(self, request, pk=None):
        pase = self.get_object()
  
        if pase.estado == 0: #Sin usar | Recoge datos de los carros y los envía
            usuario_id = pase.usuario_id
            if usuario_id is None:
                return Response({'error': 'No se encontró el usuario_id en el pase.'}, status=status.HTTP_404_NOT_FOUND)
            vehiculos = Vehiculo.objects.filter(usuarioID = usuario_id)
            if not vehiculos.exists():
                return Response({'error': 'No se encontraron vehículos para el id del usuario proporcionado.'}, status=status.HTTP_404_NOT_FOUND)
    
            vehiculos_serializados = VehiculoSerializer(vehiculos, many=True)
            pase.estado += 1
            return Response({'id_usuario': f'{usuario_id}', 'vehiculos':vehiculos_serializados.data}, status=status.HTTP_200_OK)    
        
        if pase.estado == 1:  #En proceso | Recibe el json del carro elegido
            pase.json_vehiculo = request.data.get('json_vehiculo')
            if pase.json_vehiculo is None:
                return Response({'error': 'JSON de vehículo no proporcionado'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
            vigilante_data = request.user
            apellidos= vigilante_data.apellidos
            nombres = vigilante_data.nombres
            pase.nombre_vigilante = f'{nombres} {apellidos}'
         
            pase.hora_entrada = timezone.now()

            pase.estado += 1
            pase.save()
            return Response({'status': 'Pase establecido en uso', 'id':pase.pk, 'estado':pase.estado}, status=status.HTTP_200_OK)
        elif pase.estado == 3: #En uso
            pase.hora_salida = timezone.now()            
            pase.estado += 1
            pase.save()
            return Response({'status': 'Pase completado', 'id':pase.pk, 'estado':pase.estado}, status=status.HTTP_200_OK)
        elif pase.estado == 3: #Completado
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
    
    @action(detail=False, methods=['GET'], permission_classes = [IsVigilante])
    def cedula(self, request):
        cedula_buscar = request.data.get('cc')
        if cedula_buscar == None:
            return Response({'error': 'No se proporcionó una cédula'}, status=status.HTTP_400_BAD_REQUEST)
        pases_encontrados = Pase.objects.filter(cc = cedula_buscar, estado = 2)
        if not pases_encontrados.exists():
            return Response({'error': 'No se encontró pases "en uso" del usuario'}, status=status.HTTP_404_NOT_FOUND)
        
        pases_serial = PaseSerializer(pases_encontrados, many = True)
        return Response({'status': 'Se encontró pases sin completar', "pases_encontrados": pases_serial}, status=status.HTTP_200_OK)


        
        
    


