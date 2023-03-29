from datetime import datetime
from django.db import models

from product.models import ProductModel

# Create your models here.


class DiscountModel(models.Model):
    name = models.CharField(max_length=80, blank=True)
    description = models.CharField(max_length=160, blank=True)
    rate = models.FloatField()
    start_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    end_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey(
        ProductModel, related_name='discounts', on_delete=models.CASCADE)

    def valid(self):
        if self.end_date:
            return self.start_date <= datetime.now() <= self.end_date
        else:
            return self.start_date <= datetime.now()

    def __str__(self):
        return f'{self.name} of {self.rate} on {self.product}'
