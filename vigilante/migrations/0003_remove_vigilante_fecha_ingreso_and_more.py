# Generated by Django 5.0.3 on 2024-05-19 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vigilante', '0002_vigilante_activo_vigilante_fecha_ingreso_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vigilante',
            name='fecha_ingreso',
        ),
        migrations.RemoveField(
            model_name='vigilante',
            name='fecha_salida',
        ),
    ]