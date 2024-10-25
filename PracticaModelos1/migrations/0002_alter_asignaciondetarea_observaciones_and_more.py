# Generated by Django 5.1.2 on 2024-10-24 06:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PracticaModelos1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignaciondetarea',
            name='observaciones',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='contenido',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='descripcion',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_finalizacion',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='completada',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='descripcion',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='hora_vencimiento',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
