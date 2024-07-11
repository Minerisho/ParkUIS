from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaseViewSet

router = DefaultRouter()
router.register(r'pase', PaseViewSet, basename='pase')
urlpatterns = router.urls  
