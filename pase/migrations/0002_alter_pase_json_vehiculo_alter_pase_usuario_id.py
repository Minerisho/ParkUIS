# Generated by Django 5.0.3 on 2024-07-11 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pase',
            name='json_vehiculo',
            field=models.JSONField(default=dict, verbose_name='información del vehiculo a utilizar'),
        ),
        migrations.AlterField(
            model_name='pase',
            name='usuario_id',
            field=models.FloatField(),
        ),
    ]
