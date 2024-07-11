from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VigilanteViewSet, es_vigilante

router = DefaultRouter()
router.register(r'vigilantes', VigilanteViewSet, basename='vigilante')


urlpatterns = [
    path('', include(router.urls)),
    path('es_vigilante/', es_vigilante, name='verificar si es vigilante')
    
]