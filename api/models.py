from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from shortuuid.django_fields import ShortUUIDField, ShortUUID


class ExtendedUser(AbstractUser):
    bio = models.CharField(_("Bio"), max_length=300)



class Post(models.Model):

    post_id = ShortUUIDField(primary_key=True, length=12, editable=False)
    post_content = models.CharField(_("Content"), max_length=255)
    created_on = models.DateTimeField(_("Created On"), auto_now_add=True)


    def save(self, *args, **kwargs):
        if not self.post_id:
            self.post_id = ShortUUID().random(length=12)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return f"{self.post_content[:10]}"