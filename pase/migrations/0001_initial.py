# Generated by Django 5.0.3 on 2024-07-11 07:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_entrada', models.DateTimeField(default=None, null=True, verbose_name='hora de entrada')),
                ('hora_salida', models.DateTimeField(default=None, null=True, verbose_name='hora de salida')),
                ('json_vehiculo', models.JSONField(default={}, verbose_name='información del vehiculo a utilizar')),
                ('nombre_vigilante', models.CharField(default=None, max_length=50, null=True, verbose_name='nombre del vigilante')),
                ('estado', models.CharField(choices=[(0, 'en uso'), (1, 'perdido'), (2, 'completado'), (3, 'sin usar')], default=3, max_length=10)),
                ('temporal', models.BooleanField(default=False)),
                ('usuario_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='ID del usuario(temporal)')),
            ],
            options={
                'verbose_name': 'Pase',
                'verbose_name_plural': 'Pases',
            },
        ),
    ]
