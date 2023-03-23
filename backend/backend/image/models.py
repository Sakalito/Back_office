from django.db import models

from product.models import ProduitModel

# Create your models here.


class ImageModel(models.Model):
    alt = models.CharField(max_length=80)
    img = models.ImageField(upload_to='images/')
    product = models.ForeignKey(
        ProduitModel, on_delete=models.DO_NOTHING, related_name='images')
    
    def __str__(self):
        return f'{self.alt} of {self.product}'
