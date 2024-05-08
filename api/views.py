from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import ExtendedUser, Post
from .serializers import UserSerializer, PostSerializer



class UserViewSet(ModelViewSet):
    queryset = ExtendedUser.objects.all()
    serializer_class = UserSerializer


class PostsViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer