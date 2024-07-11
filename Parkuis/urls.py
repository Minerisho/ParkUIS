
from django.contrib import admin
from django.urls import path, include
from Home.views import MensajeHome

urlpatterns = [
    path('', MensajeHome),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('pase.urls')),
    path('', include('establecimiento.urls')),
]


