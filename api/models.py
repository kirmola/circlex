from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class ExtendedUser(AbstractUser):
    bio = models.CharField(_("Bio"), max_length=300)