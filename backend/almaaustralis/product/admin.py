from django.contrib import admin
from .models import Product, Category
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ProductResourse(resources.ModelResource):
    class Meta:
        model = Product

class CategoryResourse(resources.ModelResource):
    class Meta:
        model = Category

class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("name", "category", "price", "active")
    list_filter = ("category",)
    actions = ['hide_product', 'show_product']
    resource_class = ProductResourse

    @admin.action(description='Ocultar productos seleccionado/s')
    def hide_product(self, request, queryset):
        for product in queryset:
            product.active = False
            product.save()

    @admin.action(description='Mostrar productos seleccionado/s')
    def show_product(self, request, queryset):
        for product in queryset:
            product.active = True
            product.save()

class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("name","active")
    list_filter = ("active",)
    resource_class = CategoryResourse

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)