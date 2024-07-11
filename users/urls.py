from django.urls import path, re_path, include
from . import views

urlpatterns = [
    re_path('login', views.login, name='login'),
    re_path('signup', views.signup, name='registro'),
    re_path('change_pass', views.change_pass, name='cambiar contra'),
    re_path('logout', views.logout, name='logout'),
    re_path('vehiculo/', include('vehiculos.urls')),
    re_path('', include('vigilante.urls')),
]
