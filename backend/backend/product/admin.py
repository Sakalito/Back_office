from django.contrib import admin

from .models import ProductModel

# Register your models here.


class ProduitAdminModel(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'owner',)
    list_filter = ('category', 'owner')
    search_fields = ('name', 'price', 'category', 'owner')
    list_per_page = 25


admin.site.register(ProductModel, ProduitAdminModel)
