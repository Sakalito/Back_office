from rest_framework.serializers import ModelSerializer

from discount.serializers import DiscountSerializer

from .models import CategoryModel, ProductOwnerModel, ProduitModel


class CategorySerializer(ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = (
            "id",
            "name",
            "description",
        )


class ProductOwnerSerializer(ModelSerializer):
    class Meta:
        model = ProductOwnerModel
        fields = (
            "id",
            "name",
        )


class ProduitSerializer(ModelSerializer):
    category = CategorySerializer()
    owner = ProductOwnerSerializer()
    discount = DiscountSerializer()

    class Meta:
        model = ProduitModel
        fields = (
            "id",
            "name",
            "price",
            "unit",
            "availability",
            "comments",
            "category",
            "owner",
        )
