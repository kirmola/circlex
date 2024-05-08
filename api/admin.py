from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ExtendedUser, Post

admin.site.register(ExtendedUser, UserAdmin)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
