# Generated by Django 5.1.2 on 2024-10-10 09:06

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('descripcion', models.TextField()),
                ('duracion_estimada', models.FloatField()),
                ('fecha_inicio', models.DateField(default=django.utils.timezone.now)),
                ('fecha_finalizacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('correo_electronico', models.CharField(max_length=200, unique=True)),
                ('contraseña', models.CharField(max_length=200)),
                ('fecha_registro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('descripcion', models.TextField()),
                ('prioridad', models.IntegerField()),
                ('estado', models.CharField(choices=[('Pend', 'Pendiente'), ('Pro', 'Progreso'), ('Com', 'Completada')], default='Pendiente', max_length=50)),
                ('completada', models.BooleanField()),
                ('fecha_creacion', models.DateField(default=django.utils.timezone.now)),
                ('hora_vencimiento', models.TimeField()),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PracticaModelos1.proyecto')),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creador', to='PracticaModelos1.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True)),
                ('tarea', models.ManyToManyField(to='PracticaModelos1.tarea')),
            ],
        ),
        migrations.CreateModel(
            name='AsignacionDeTarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observaciones', models.TextField()),
                ('fecha_asignacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PracticaModelos1.tarea')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PracticaModelos1.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='tarea',
            name='usuario',
            field=models.ManyToManyField(related_name='usuario', through='PracticaModelos1.AsignacionDeTarea', to='PracticaModelos1.usuario'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='Asignaciones',
            field=models.ManyToManyField(related_name='ProyectosAsignados', to='PracticaModelos1.usuario'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='creador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PracticaModelos1.usuario'),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha_comentario', models.DateTimeField(default=django.utils.timezone.now)),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PracticaModelos1.tarea')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PracticaModelos1.usuario')),
            ],
        ),
    ]
