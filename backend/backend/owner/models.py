from django.db import models

# Create your models here.


class ProductOwnerModel(models.Model):
    name = models.CharField(max_length=80)
