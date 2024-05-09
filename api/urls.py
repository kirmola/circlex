from django.urls import path, include
from rest_framework import routers
from api import views




router = routers.DefaultRouter()
router.register("users", views.UserViewSet, basename="root-users-all")
router.register("posts", views.PostsViewSet, basename="root-posts-all")
router.register("comments", views.CommentViewSet, basename="root-comments-all")


urlpatterns = [
    path("", include(router.urls)),
]
