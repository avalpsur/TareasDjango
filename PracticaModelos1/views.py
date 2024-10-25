from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')


def listar_proyectos(request):
    proyectos = Proyecto.objects.select_related("creador").prefetch_related("Asignaciones")
    proyectos = proyectos.all()
    return render(request,'proyecto/lista.html',{"proyectos_mostrar":proyectos})


def listar_tareas_proyecto(request,id_proyecto):
    tareas = Tarea.objects.select_related("creador","proyecto").prefetch_related("usuario")
    tareas = tareas.filter(proyecto_id=id_proyecto).order_by("-fecha_creacion").all()
    return render(request, 'tarea/lista.html',{"tareas_mostrar":tareas})


def listar_usuarios_tarea(request,id_tarea):
    usuarios = Usuario.objects.filter(asignaciondetarea__tarea=id_tarea).order_by("asignaciondetarea__fecha_asignacion").all()
    return render(request, 'usuario/lista.html',{"usuarios_mostrar":usuarios})


def listar_tareas_observaciones(request,texto_tarea):
    tareas = Tarea.objects.filter(asignaciondetarea__observaciones__contains=texto_tarea).all()
    return render(request, 'tarea/lista.html',{"tareas_mostrar":tareas})


def listar_tareas_intervalo(request,ano_inicio,ano_fin,estado):
    tareas = Tarea.objects.filter(
        fecha_creacion__year__gte=ano_inicio,
        fecha_creacion__year__lte=ano_fin,
        estado=estado,
    ).all()
    return render(request, 'tarea/lista.html',{"tareas_mostrar":tareas})


def listar_ultimoUsuario(request,id_tarea):
    usuario = Usuario.objects.filter(asignaciondetarea__tarea__id=id_tarea).order_by("-comentario__fecha_comentario")[:1].get()
    return render(request, 'usuario/usuario.html',{"usuario":usuario})