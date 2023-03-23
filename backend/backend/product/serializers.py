from rest_framework.serializers import ModelSerializer

from owner.serializers import ProductOwnerSerializer
from category.serializers import CategorySerializer
from discount.serializers import DiscountSerializer

from .models import ProduitModel


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
