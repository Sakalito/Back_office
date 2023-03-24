from rest_framework import serializers

from .models import ImageModel


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = (
            "id",
            "alt",
            "img",
            "product",
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # data["product"] = instance.product.id
        data.pop("product")
        data.pop("img")
        return data
