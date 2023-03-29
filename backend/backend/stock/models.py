from datetime import datetime
from django.db import models

from product.models import ProductModel

# Create your models here.

_stockMoveTypes = ['IN', 'OUT']


class StockMoveModel(models.Model):
    date = models.DateTimeField(default=datetime.now())
    type = models.CharField(choices=[(x, x)
                            for x in _stockMoveTypes], max_length=3,)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True,)

    def products(self):
        return self.items.all()

    def calculate_update_price(self):
        total = 0
        for item in self.items.all():
            # if there is a valid discount on product
            if item.product.discount() and item.product.discount().valid:
                total += item.product.discounted_price() * item.amount
            else:
                total += item.product.price * item.amount
        self.price = total
        self.save()

    def __str__(self):
        return f"{self.date} - {self.type}"


class StockMoveItemModel(models.Model):
    product = models.ForeignKey(
        ProductModel, on_delete=models.CASCADE, related_name="stock_move_items",
    )
    amount = models.PositiveIntegerField()
    stock_move = models.ForeignKey(
        StockMoveModel,
        on_delete=models.CASCADE,
        related_name="items",
    )

    def __str__(self):
        return f"{self.product.name} - {self.amount}"
