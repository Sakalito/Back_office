from django.db import models

from product.models import ProduitModel

# Create your models here.

class DiscountModel(models.Model):
    name = models.CharField(max_length=80, blank=True)
    description = models.CharField(max_length=160, blank=True)
    rate = models.FloatField()
    start_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    end_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey(ProduitModel, related_name='discounts', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} of {self.rate} on {self.product}'
