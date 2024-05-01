from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('login', views.login, name='login'),
    re_path('signup', views.signup, name='registro'),
    re_path('test_token', views.test_token, name='test token'),
    re_path('change_pass', views.change_pass, name='cambiar contra'),
    re_path('logout', views.logout, name='logout')
]
