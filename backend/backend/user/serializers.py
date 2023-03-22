from rest_framework.serializers import ModelSerializer
from .models import UserModel


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
        )

# USENAME = "leandre", PWD = "s3JGZ8vNm8H8h-i"
