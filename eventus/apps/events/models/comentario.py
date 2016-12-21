from django.db import models
from .categoria import TimeStampModel
from .evento import Evento
from django.conf import settings


class Comentarios(TimeStampModel):

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL)
    evento = models.ForeignKey(Evento)

    contenido = models.TextField()

    class Meta:
        verbose_name = "Comentarios"
        verbose_name_plural = "Comentarioss"

    def __str__(self):
        return "%s %s" % (self.usuario.nombreusuario, self.evento.nombre)
