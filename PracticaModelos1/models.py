from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=150)
    correo_electronico = models.CharField(max_length=200,unique=True)
    contraseña = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(default=timezone.now)

    
class Proyecto(models.Model):
    nombre = models.CharField(max_length=250) 
    descripcion = models.TextField(max_length=500)  
    duracion_estimada = models.FloatField() 
    fecha_inicio = models.DateField(default=timezone.now) 
    fecha_finalizacion = models.DateField(default=timezone.now) 
    
    Asignaciones = models.ManyToManyField(Usuario,related_name="ProyectosAsignados")
    creador = models.ForeignKey(Usuario,on_delete = models.CASCADE)

class Tarea(models.Model):
    titulo = models.CharField(max_length=250) 
    descripcion = models.TextField(max_length=500) 
    prioridad = models.IntegerField()
    
    ESTADOS = [
        ("Pend","Pendiente"),
        ("Pro","Progreso"),
        ("Com","Completada"),
    ]
    estado = models.CharField(max_length=50,choices=ESTADOS,default='Pendiente')
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateField(default=timezone.now)
    hora_vencimiento = models.TimeField(default=timezone.now) 
    
    creador = models.ForeignKey(Usuario, related_name="creador", on_delete = models.CASCADE)
    
    proyecto=models.ForeignKey(Proyecto, related_name="proyecto_tareas", on_delete = models.CASCADE)
    
    usuario = models.ManyToManyField(Usuario, related_name="usuario",through='AsignacionDeTarea')


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=255, unique=True) 
    tarea = models.ManyToManyField(Tarea)
    
class AsignacionDeTarea(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    tarea = models.ForeignKey(Tarea, on_delete = models.CASCADE)
    
    observaciones = models.TextField(max_length=500) 
    fecha_asignacion = models.DateTimeField(default=timezone.now)

class Comentario(models.Model):
    contenido = models.TextField(max_length=500)  
    fecha_comentario = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(Usuario,on_delete = models.CASCADE)
    tarea = models.ForeignKey(Tarea,on_delete = models.CASCADE)