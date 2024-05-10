from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import DetailView
from api.models import *


class UserView(DetailView):
    template_name = "user.html"
    model = ExtendedUser
    slug_field = "username"
    slug_url_kwarg = "username"
    
    def get_queryset(self):
        return super().get_queryset().only("username", "first_name", "last_name", "date_joined", "bio", "profile_picture")    
    
class PostView(DetailView):
    template_name = "posts.html"
    model = Post
    slug_field = "post_id"
    slug_url_kwarg = "post_id"


    def get_queryset(self):
        return super().get_queryset().select_related("post_author").only("post_id", "created_on", "post_content", "post_author__username", "post_author__first_name", "post_author__last_name", "post_author__profile_picture")
    

