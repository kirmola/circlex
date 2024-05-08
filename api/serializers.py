from rest_framework.serializers import ModelSerializer
from api.models import ExtendedUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = ExtendedUser
        exclude = ["password", "is_superuser", "is_staff", "is_active", "groups", "user_permissions"]