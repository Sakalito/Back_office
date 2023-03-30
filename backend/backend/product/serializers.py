from rest_framework import serializers

from image.serializers import ImageSerializer
from owner.serializers import ProductOwnerSerializer
from category.serializers import CategorySerializer
from discount.serializers import DiscountSerializer

from image.models import ImageModel
from owner.models import ProductOwnerModel
from category.models import CategoryModel
from discount.models import DiscountModel

from .models import ProductModel


class ProduitSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    # owner = ProductOwnerSerializer()
    discount = DiscountSerializer(allow_null=True, required=False)

    images = ImageSerializer(many=True, required=False)

    category = serializers.PrimaryKeyRelatedField(
        queryset=CategoryModel.objects.all(), required=True)
    owner = serializers.PrimaryKeyRelatedField(
        queryset=ProductOwnerModel.objects.all(), required=False)
    owner_from_name = serializers.CharField(required=False)
    # discount = serializers.PrimaryKeyRelatedField(queryset=DiscountModel.objects.all(), required=False)

    class Meta:
        model = ProductModel
        fields = (
            "id",
            "name",
            "price",
            "unit",
            "availability",
            "comments",
            "category",
            "owner",
            "owner_from_name",
            "discount",
            "images",
        )
        # set discount and images to optional
        extra_kwargs = {
            "discount": {"required": False},
            "images": {"required": False},
        }

    def create(self, validated_data):
        discount_data = validated_data.pop("discount", None)
        images_data = validated_data.pop("images", None)

        owner_from_name = validated_data.pop("owner_from_name", None)

        if owner_from_name:
            owner, _ = ProductOwnerModel.objects.get_or_create(
                name=owner_from_name)
            validated_data.pop("owner", None)
            product = ProductModel.objects.create(
                owner=owner, **validated_data)
        else:
            product = ProductModel.objects.create(**validated_data)

        if discount_data:
            DiscountModel.objects.create(product=product, **discount_data)
        if images_data:
            for image_data in images_data:
                ImageModel.objects.create(product=product, **image_data)

        return product

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["category"] = CategorySerializer(instance.category).data['name']
        data["owner"] = ProductOwnerSerializer(instance.owner).data['name']
        data["images"] = [image['id']
                          for image in ImageSerializer(instance.images.all(), many=True).data]
        discount = DiscountModel.objects.filter(
            product=instance).order_by("start_date").last()
        if discount:
            data["discount"] = DiscountSerializer(discount).data['rate']
        return data
