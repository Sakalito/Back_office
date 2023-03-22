from django.contrib import admin

from .models import ProduitModel, ProductOwnerModel, CategoryModel

# Register your models here.

admin.site.register(ProduitModel)
admin.site.register(ProductOwnerModel)
admin.site.register(CategoryModel)
