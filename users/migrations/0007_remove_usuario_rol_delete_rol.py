# Generated by Django 5.0.3 on 2024-05-04 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_usuario_rol'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='rol',
        ),
        migrations.DeleteModel(
            name='Rol',
        ),
    ]
