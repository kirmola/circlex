from django.urls import path, include
from rest_framework_nested import routers
from api import views




router = routers.DefaultRouter()
router.register("users", views.UserViewSet, basename="root-users-all")
router.register("posts", views.PostsViewSet, basename="root-posts-all")

user_router = routers.NestedDefaultRouter(router, r"users", lookup="user")
user_router.register(r"posts", views.SpecificPostsViewSet, basename="specific-post")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(user_router.urls)),
]
