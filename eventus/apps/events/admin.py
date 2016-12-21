from django.contrib import admin
from .models.asistente import Asistente
from .models.categoria import Categoria
from .models.comentario import Comentarios
from .models.evento import Evento
from .models.registro import Registro
# Register your models here.

admin.site.register(Asistente)
admin.site.register(Categoria)
admin.site.register(Comentarios)
admin.site.register(Evento)
admin.site.register(Registro)
