from rest_framework.serializers import ModelSerializer
from api.models import ExtendedUser, Post, Comment


class UserSerializer(ModelSerializer):
    class Meta:
        model = ExtendedUser
        exclude = ["password", "is_superuser", "is_staff", "is_active", "groups", "user_permissions"]


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"