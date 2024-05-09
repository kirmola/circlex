from django.urls import path
from .views import *

urlpatterns = [
    path("<str:username>/", UserView.as_view(), name="user-profile"),
    path("p/<str:post_id>/", PostView.as_view(), name="post-view")
]
