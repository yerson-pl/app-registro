from django.db import models
from .categoria import TimeStampModel
from .evento import Evento
from django.conf import settings


class Asistente(TimeStampModel):
    # falta crear modelo usuario
    asistente = models.ForeignKey(settings.AUTH_USER_MODEL)
    evento = models.ManyToManyField(Evento)
    asistio = models.BooleanField(default=False)
    ha_pagado = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Asistente"
        verbose_name_plural = "Asistentes"

    def __str__(self):
        return "%s %s" % (self.asistente.nombreusuario, self.evento.nombre)
