from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'editar/(?P<pk>\d+)$', views.editar_vehiculo, name='update-vehiculo'),
    re_path('mis-vehiculos', views.ver_mis_vehiculos, name='ver-mis-vehiculos'),
    re_path('crear', views.crear_vehiculo, name='crear-vehiculo')
]
