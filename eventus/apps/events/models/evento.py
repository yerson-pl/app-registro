from django.db import models
from .categoria import TimeStampModel, Categoria
from django.conf import settings
from django.template.defaultfilters import slugify


def upload_location(instance, filename):
    return "%s %s " % (instance.id, filename)


class Evento(TimeStampModel):
    nombre = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(editable=False)
    resumen = models.TextField(max_length=255)
    contenido = models.TextField()
    categoria = models.ForeignKey(Categoria)
    lugar = models.CharField(max_length=50)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    imagen = models.ImageField(upload_to=upload_location,
                               null=True, blank=True,
                               height_field="height_field",
                               width_field="width_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    es_libre = models.BooleanField(default=True)
    costo = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    numero_visitas = models.PositiveIntegerField(default=0)
    organizador = models.ForeignKey(
        settings.AUTH_USER_MODEL)  # Falta crear  Usuarios

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.nombre)
        super(Evento, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        return self.nombre
