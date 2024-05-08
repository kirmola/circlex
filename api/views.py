from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import ExtendedUser
from .serializers import UserSerializer



class UserViewSet(ModelViewSet):
    queryset = ExtendedUser.objects.all()
    serializer_class = UserSerializer


# class PostsViewSet(ModelViewSet):
#     queryset = ExtendedUser.objects.all()