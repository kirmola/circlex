from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api.models import (
    ExtendedUser, 
    Post,
    Comment
)
from api.serializers import UserSerializer, PostSerializer, CommentSerializer
from django.shortcuts import get_list_or_404


class UserViewSet(ModelViewSet):
    queryset = ExtendedUser.objects.all()
    serializer_class = UserSerializer


class PostsViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer