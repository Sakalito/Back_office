from rest_framework.serializers import ModelSerializer
from .models import DiscountModel


class DiscountSerializer(ModelSerializer):
    class Meta:
        model = DiscountModel
        fields = (
            "name",
            "description",
            "rate",
            "start_date",
            "end_date",
        )
