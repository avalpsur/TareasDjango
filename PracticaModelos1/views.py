from django.shortcuts import render
from django.db.models import Prefetch
from .models import *
from django.views.defaults import page_not_found

# Create your views here.

def index(request):
    return render(request, 'index.html')


def listar_proyectos(request):
    proyectos = Proyecto.objects.select_related("creador").prefetch_related("Asignaciones",Prefetch("proyecto_tareas")).all()
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


def listar_ultimoUsuario(request,id_proyecto):
    usuario = Usuario.objects.filter(comentario__tarea__proyecto=id_proyecto).order_by("-comentario__fecha_comentario")[:1].get()
    return render(request, 'usuario/usuario.html',{"usuario":usuario})


def listar_comentarios(request,palabra,fecha,id_tarea):
    comentarios = Comentario.objects.filter(tarea=id_tarea,contenido__startswith=palabra,fecha_comentario__year=fecha).all()
    return render(request, 'comentario/lista.html',{"comentario":comentarios})


def listar_etiquetas(request,id_proyecto):
    etiquetas = Etiqueta.objects.filter(tarea__proyecto=id_proyecto).all()
    return render(request, 'etiqueta/lista.html',{"etiqueta":etiquetas})


def listar_usuarios_sinTarea(request):
    usuarios = Usuario.objects.filter(asignaciondetarea=None)
    return render(request, 'usuario/lista.html',{"usuarios_mostrar":usuarios})

def error_404(request, exception=None):
    return render(request, 'errores/404.html',None,None,404)

def error_500(request,exception = None):
    return render(request, 'errores/500.html',None,None,500)

def error_403(request, exception=None):
    return render(request, 'errores/403.html',None,None,403)

def error_400(request, exception=None):
    return render(request, 'errores/400.html',None,None,400)