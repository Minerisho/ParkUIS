from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



class Rol(models.Model):
    nombre_rol = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre_rol

class UsuarioManager(BaseUserManager):
    def _create_user(self, email, password, nombres, apellidos, num_cel, rol, **extra_fields):
        if not email:
            raise ValueError("Debe ingresar un correo electrónico")
        if not password:
            raise ValueError('Debe ingresar una contraseña')

        user = self.model(
            email = self.normalize_email(email),
            nombres = nombres,
            apellidos = apellidos,
            num_cel = num_cel,
            rol = rol,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, nombres, apellidos, num_cel, rol, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email, password, nombres, apellidos, num_cel, rol, **extra_fields)

    def create_superuser(self, email, password, nombres, apellidos, num_cel, rol, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email, password, nombres, apellidos, num_cel, rol, **extra_fields)
    

    

class Usuario(AbstractBaseUser, PermissionsMixin):
    # password, last_login, is_active ya vienen incluído en la promo con un 10% de descuento usando la tarjeta falabella
    email = models.EmailField(unique=True, max_length=200, db_index=True)
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    CC = models.BigIntegerField(unique=True, verbose_name=("número de cédula"))
    num_cel = models.BigIntegerField(unique=True, verbose_name=("número de celular"))
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    rol = models.ForeignKey(to = Rol, on_delete=models.CASCADE)
    objects = UsuarioManager()
    
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombres', 'apellidos', 'CC', 'num_cel', 'rol']
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    def __str__(self):
        return self.email
    




    
