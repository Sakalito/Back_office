from django.contrib import admin

from .models import StockMoveModel, StockMoveItemModel

# Register your models here.


class StockMoveItemAdminModel(admin.ModelAdmin):
    list_display = ('id', 'product', 'amount', 'stock_move',)
    list_filter = ('stock_move',)
    search_fields = ('product', 'amount', 'stock_move',)
    list_per_page = 25


class StockMoveAdminModel(admin.ModelAdmin):
    list_display = ('id', 'date', 'type',)
    list_filter = ('date', 'type',)
    search_fields = ('date', 'type',)
    list_per_page = 25


admin.site.register(StockMoveItemModel, StockMoveItemAdminModel)
admin.site.register(StockMoveModel, StockMoveAdminModel)
