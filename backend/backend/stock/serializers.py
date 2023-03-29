from rest_framework import serializers

from .models import StockMoveItemModel, StockMoveModel


class StockMoveItemSerializer(serializers.ModelSerializer):
    stock_move = serializers.PrimaryKeyRelatedField(
        queryset=StockMoveModel.objects.all(),
        required=False,
    )

    class Meta:
        model = StockMoveItemModel
        fields = "__all__"
        # set stock_move to optional
        extra_kwargs = {
            "stock_move": {"required": False},
        }

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop("stock_move")
        return data


class StockMoveSerializer(serializers.ModelSerializer):
    products = StockMoveItemSerializer(many=True)

    class Meta:
        model = StockMoveModel
        fields = (
            "id",
            "date",
            "type",
            "products",
        )

    def create(self, validated_data):
        items_data = validated_data.pop("products")
        stock_move = StockMoveModel.objects.create(**validated_data)
        for item_data in items_data:
            StockMoveItemModel.objects.create(
                stock_move=stock_move, **item_data)
        return stock_move

    items_field_name = "products"  # "items"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data[self.items_field_name] = StockMoveItemSerializer(
            instance.items.all(), many=True).data
        return data
