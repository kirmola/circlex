from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api.models import (
    ExtendedUser, 
    Post,
    Comment
)
from api.serializers import UserSerializer, PostSerializer, CommentSerializer
from django.shortcuts import get_list_or_404, get_object_or_404


class UserViewSet(ModelViewSet):
    queryset = ExtendedUser.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return get_object_or_404(ExtendedUser, username=self.kwargs.get("pk"))


class PostsViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer