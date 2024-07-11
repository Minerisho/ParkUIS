from rest_framework.permissions import BasePermission
from .models import Vigilante

class IsVigilante(BasePermission):
    """
    Permite el acceso solo a los vigilantes.
    """

    def has_permission(self, request, view):
        # Asegura que solo los vigilantes activos puedan acceder
        return Vigilante.objects.filter(usuario_id=request.user.id, activo=True).exists()
