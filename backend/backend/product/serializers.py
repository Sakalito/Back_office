from rest_framework import serializers

from owner.serializers import ProductOwnerSerializer
from category.serializers import CategorySerializer
from discount.serializers import DiscountSerializer

from owner.models import ProductOwnerModel
from category.models import CategoryModel
from discount.models import DiscountModel

from .models import ProduitModel


class ProduitSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    # owner = ProductOwnerSerializer()
    discount = DiscountSerializer(allow_null=True, required=False)

    category = serializers.PrimaryKeyRelatedField(
        queryset=CategoryModel.objects.all(), required=True)
    owner = serializers.PrimaryKeyRelatedField(
        queryset=ProductOwnerModel.objects.all(), required=True)
    # discount = serializers.PrimaryKeyRelatedField(queryset=DiscountModel.objects.all(), required=False)

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
            "discount",
        )
        # set discount to optional
        extra_kwargs = {
            "discount": {"required": False},
        }

    def create(self, validated_data):
        discount_data = validated_data.pop("discount", None)
        product = ProduitModel.objects.create(**validated_data)
        if discount_data:
            DiscountModel.objects.create(product=product, **discount_data)
        return product

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["category"] = CategorySerializer(instance.category).data
        data["owner"] = ProductOwnerSerializer(instance.owner).data
        # discount = DiscountModel.objects.filter(product=instance).order_by("start_date").last()
        # if discount: data["discount"] = DiscountSerializer(discount).data
        return data
