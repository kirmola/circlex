from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api.models import (
    ExtendedUser, 
    Post
)
from api.serializers import UserSerializer, PostSerializer
from django.shortcuts import get_list_or_404


class UserViewSet(ModelViewSet):
    queryset = ExtendedUser.objects.all()
    serializer_class = UserSerializer


class PostsViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class SpecificPostsViewSet(ModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        user_pk = self.kwargs.get("user_pk")
        post_id = self.kwargs.get("pk")
        return get_list_or_404(Post, post_author=user_pk)
