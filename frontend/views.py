from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView
from api.models import *


class UserView(TemplateView):
    template_name = "user.html"
    # model = ExtendedUser
    # slug_field = "username"
    # slug_url_kwarg = "username"
    
    # def get_queryset(self):
    #     return super().get_queryset().only("first_name", "last_name", "date_joined", "bio")
    
class PostView(TemplateView):
    template_name = "posts.html"
    # model = Post
    # slug_field = "post_id"
    # slug_url_kwarg = "post_id"    

