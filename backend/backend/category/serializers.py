from rest_framework.serializers import ModelSerializer

from .models import CategoryModel


class CategorySerializer(ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = (
            "id",
            "name",
            "description",
        )
