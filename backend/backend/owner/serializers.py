from rest_framework.serializers import ModelSerializer

from .models import ProductOwnerModel

class ProductOwnerSerializer(ModelSerializer):
    class Meta:
        model = ProductOwnerModel
        fields = (
            "id",
            "name",
        )