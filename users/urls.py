from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('login', views.login),
    re_path('signup', views.signup),
    re_path('test_token', views.test_token),
    re_path('change_pass', views.change_pass),
    re_path('logout', views.logout)
]
