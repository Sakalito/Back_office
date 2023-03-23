from django.contrib import admin

# Register your models here.

from .models import CategoryModel

class CategoryAdminModel(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(CategoryModel, CategoryAdminModel)