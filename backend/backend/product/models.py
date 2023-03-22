from django.db import models

# Create your models here.


class ProductOwnerModel(models.Model):
    name = models.CharField(max_length=80)


class CategoryModel(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=160, blank=True)


class ProduitModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    comments = models.CharField(max_length=150, blank=True)
    unit = models.CharField(max_length=12)
    availability = models.BooleanField(default=False)
    price = models.FloatField()
    owner = models.ForeignKey(
        ProductOwnerModel, on_delete=models.DO_NOTHING, related_name='products')
    category = models.ForeignKey(
        CategoryModel, on_delete=models.DO_NOTHING, related_name='products')
