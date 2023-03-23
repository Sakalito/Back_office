from django.contrib import admin

from .models import ProductOwnerModel

# Register your models here.


class ProductOwnerAdminModel(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(ProductOwnerModel, ProductOwnerAdminModel)
