from django.db import models

from product.models import ProductModel

# Create your models here.

_stockMoveTypes = ['IN', 'OUT']


class StockMoveModel(models.Model):
    date = models.DateField()
    type = models.CharField(choices=[(x, x)
                            for x in _stockMoveTypes], max_length=3,)

    def __str__(self):
        return f"{self.date} - {self.type}"


class StockMoveItemModel(models.Model):
    product = models.ForeignKey(
        ProductModel, on_delete=models.CASCADE, related_name="stock_move_items",
    )
    quantity = models.IntegerField()
    stock_move = models.ForeignKey(
        StockMoveModel,
        on_delete=models.CASCADE,
        related_name="items",
    )

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"
