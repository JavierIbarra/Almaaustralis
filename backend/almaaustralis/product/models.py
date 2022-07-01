from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name="Nombre")
    active = models.BooleanField(default=True, verbose_name="Activo")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nombre")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Categoria")
    description = models.TextField(verbose_name="Descripcion")
    url_image = models.URLField(verbose_name="URL image", null=True, blank=True)
    price = models.IntegerField(verbose_name="Precio")
    stock = models.IntegerField(verbose_name="Stock", null=True)
    active = models.BooleanField(default=False, verbose_name="Mostrar")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.name