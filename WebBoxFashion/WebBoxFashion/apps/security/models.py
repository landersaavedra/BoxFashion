import os
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django import forms
from django.utils.translation import ugettext as _


@receiver(user_signed_up)
def create_user_profile(request, user, **kwargs):
    profile = Profile.objects.create(user=user)
    profile.save()



class Login_Customer(models.Model):
    sname = models.CharField(max_length=100,blank=False, verbose_name='Nombre')
    semail = models.CharField(max_length=150, blank=False, verbose_name='Email')
    scontrasenia = models.CharField(max_length=10, blank=False, verbose_name='Contraseña')
    bis_active = models.BooleanField(verbose_name='Activacion del Cliente')
    dtimestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sname

    class Meta:
        ordering = ('sname',)
        verbose_name = _("Login Cliente")
        verbose_name_plural = _("Login Clientes")

class Login_Partner(models.Model):
    sname = models.CharField(max_length=100,blank=False, verbose_name='Socio')
    semail = models.CharField(max_length=150, blank=False, verbose_name='Email')
    scontrasenia = models.CharField(max_length=10, blank=False, verbose_name='Contraseña')
    bis_active = models.BooleanField(verbose_name='Activacion del Cliente')
    dtimestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sname

    class Meta:
        ordering = ('sname',)
        verbose_name = _("Login de Socio")
        verbose_name_plural = _("Login de Socios")

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