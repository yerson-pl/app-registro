from django.db import models
from django.template.defaultfilters import slugify


class TimeStampModel(models.Model):

    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateField(auto_now=True)

    class Meta:
        abstract = True
        verbose_name = "TimeStampModel"
        verbose_name_plural = "TimeStampModels"


class Categoria(models.Model):

    nombre = models.CharField(max_length=50)
    slug = models.SlugField(editable=False)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def save(self, *args, **kwargs):
        if not self.id:
                    self.slug = slugify(self.nombre)
        super(Categoria, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre
