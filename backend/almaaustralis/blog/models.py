from django.db import models
from django.utils.timezone import now
from users.models import User
from ckeditor.fields import RichTextField

class Tema(models.Model):
    name = models.CharField(max_length=20, verbose_name="nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "tema"
        verbose_name_plural = "temas"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = RichTextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de publicacion", default=now)
    url_image = models.URLField(verbose_name="URL image", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    tema = models.ManyToManyField(Tema, verbose_name="Temas")
    active = models.BooleanField(verbose_name="Mostrar", default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-created']


class PostComment(models.Model):
    post = models.ForeignKey(Post, related_name='Post', verbose_name="Post", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Contenido")
    active = models.BooleanField(verbose_name="Mostrar", default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Comentario Post"
        verbose_name_plural = "Comentarios Post"
        ordering = ['-created']
    
    def __str__(self):
        return self.content

