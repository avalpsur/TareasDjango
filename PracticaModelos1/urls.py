from django.urls import path
from .import views


urlpatterns = [
    path('',views.index,name='index'),
    path('proyectos/listar',views.listar_proyectos,name='lista_proyectos'),
    path('tareas/listar/<int:id_proyecto>', views.listar_tareas_proyecto,name='lista_tareas_proyecto'),
    path('usuario/listar/<int:id_tarea>', views.listar_usuarios_tarea, name='lista_usuarios_tarea'),
    path('tareas/listar/<str:texto_tarea>',views.listar_tareas_observaciones, name='lista_tareas_observacion'),
    path('tareas/listar/<int:ano_inicio>/<int:ano_fin>/<str_completada>',views.listar_tareas_intervalo, name='lista_tareas_intervalo'),
]   