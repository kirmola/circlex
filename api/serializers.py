from rest_framework.serializers import ModelSerializer
from api.models import ExtendedUser, Post


class UserSerializer(ModelSerializer):
    class Meta:
        model = ExtendedUser
        exclude = ["password", "is_superuser", "is_staff", "is_active", "groups", "user_permissions"]


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"