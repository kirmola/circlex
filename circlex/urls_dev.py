from .urls import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns += [
    path("__reload__/", include("django_browser_reload.urls")),
    path("__debug__/", include("debug_toolbar.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)