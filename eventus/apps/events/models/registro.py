from django.db import models
from .categoria import TimeStampModel
from ..choices.enums import GENERO_CHOICES, PROVINCIAS_CHOICES, ENTERECE_CHOICES


class Registro(TimeStampModel):
    nombre = models.CharField(max_length=80)
    apellidos = models.CharField(max_length=150)
    email = models.EmailField()
    celular = models.CharField(max_length=9)
    organizacion = models.CharField(max_length=150)
    provincia = models.CharField(max_length=100, choices=PROVINCIAS_CHOICES)
    distrito = models.CharField(max_length=100)
    genero = models.CharField(
        max_length=40, choices=GENERO_CHOICES, blank=True)
    edad = models.IntegerField()
    me_entere = models.CharField(
        max_length=60, choices=ENTERECE_CHOICES, blank=True)

    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"

    def __str__(self):
        return self.nombre
