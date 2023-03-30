from django.db import models
from owner.models import ProductOwnerModel
from category.models import CategoryModel

# Create your models here.


class ProduitModel(models.Model):
    name = models.CharField(max_length=80)
    comments = models.CharField(max_length=150, blank=True)
    unit = models.CharField(max_length=12)
    availability = models.BooleanField(default=False)
    price = models.FloatField()
    owner = models.ForeignKey(
        ProductOwnerModel, on_delete=models.DO_NOTHING, related_name='products')
    category = models.ForeignKey(
        CategoryModel, on_delete=models.DO_NOTHING, related_name='products')
    
    def discount(self):
        return self.discounts.order_by('start_date').last()
    
    def __str__(self):
        return f'{self.name} of {self.owner} in {self.category} at {self.price} per {self.unit}'
