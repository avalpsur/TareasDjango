from django.contrib import admin
from .models import Usuario
from .models import Proyecto
from .models import Tarea
from .models import Etiqueta
from .models import AsignacionDeTarea
from .models import Comentario

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Proyecto)
admin.site.register(Tarea)
admin.site.register(Etiqueta)
admin.site.register(AsignacionDeTarea)
admin.site.register(Comentario)