import os
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone


class UserProfile(models.Model):

    def image_path(self, filename):
        extension = os.path.splitext(filename)[1][1:]
        file_name = os.path.splitext(filename)[0]
        url = "Users/%s/profile/%s.%s" % (self.user.id, slugify(str(file_name)), extension)
        return url

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image_profile = models.ImageField(upload_to=image_path, null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()


# ============================================================
# Conectamos signals.
# ============================================================

from .signals import *