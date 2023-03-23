from django.db import models

# Create your models here.


class CategoryModel(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=160, blank=True)
