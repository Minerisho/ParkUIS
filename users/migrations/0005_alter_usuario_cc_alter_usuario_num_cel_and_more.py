# Generated by Django 5.0.3 on 2024-04-20 18:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_usuario_cc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='CC',
            field=models.BigIntegerField(unique=True, verbose_name='número de cédula'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='num_cel',
            field=models.BigIntegerField(unique=True, verbose_name='número de celular'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.rol'),
        ),
    ]