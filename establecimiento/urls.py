from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EstablecimientoVieSet

router = DefaultRouter()
router.register(r'establecimientos', EstablecimientoVieSet, basename='establecimiento')


urlpatterns = [
    path('', include(router.urls))
    
]