from django.http import HttpResponseForbidden
from functools import wraps
from vigilante.models import Vigilante  

def vigilante_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if Vigilante.objects.filter(usuario_id=request.user.id).exists():
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Acceso denegado: No tienes permisos de vigilante.")
    return _wrapped_view
