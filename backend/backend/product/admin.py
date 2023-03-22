from django.contrib import admin

from .models import ProduitModel, ProductOwnerModel, CategoryModel

# Register your models here.


class ProduitAdminModel(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'owner',)
    list_filter = ('category', 'owner')
    search_fields = ('name', 'price', 'category', 'owner')
    list_per_page = 25


class ProductOwnerAdminModel(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 25


class CategoryAdminModel(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(ProduitModel, ProduitAdminModel)
admin.site.register(ProductOwnerModel, ProductOwnerAdminModel)
admin.site.register(CategoryModel, CategoryAdminModel)
