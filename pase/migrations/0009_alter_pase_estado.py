# Generated by Django 5.0.3 on 2024-07-11 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pase', '0008_alter_pase_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pase',
            name='estado',
            field=models.FloatField(choices=[(0, 'sin usar'), (1, 'en uso'), (2, 'completado'), (3, 'perido')], default=0, max_length=10),
        ),
    ]
