# Generated by Django 5.0.3 on 2024-07-11 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pase', '0004_alter_pase_json_vehiculo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pase',
            name='json_vehiculo',
            field=models.JSONField(default=dict, null=True, verbose_name='información del vehiculo a utilizar'),
        ),
    ]