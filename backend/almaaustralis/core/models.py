from email.policy import default
from django.db import models

# Create your models here.
class SocialNetworks(models.Model):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=30 , verbose_name="Nombre")
    link = models.URLField(verbose_name="Link")
    logo_class = models.CharField(max_length=15, verbose_name="Nombre logo")
    
    class Meta:
        verbose_name = "Red Social"
        verbose_name_plural = "Redes Sociales"

class TextInfo(models.Model):
    title = models.CharField(max_length=40, verbose_name="Titulo")
    text = models.TextField( verbose_name="Texto")
    url_image = models.URLField(verbose_name="URL image")

    class Meta:
        verbose_name = "Texto informativo"
        verbose_name_plural = "Textos informativos"

class Carousel(models.Model):
    active = models.BooleanField(default=True)
    initial_class = models.CharField(max_length=40, null=True, blank=True)
    info = models.CharField(max_length=20, null=True, blank=True)
    url_image = models.URLField(verbose_name="URL image")

    class Meta:
        verbose_name = "Imagen Deslizante"
        verbose_name_plural = "Imagenes Deslizantes"