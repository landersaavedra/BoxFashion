from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile


@receiver(post_save, sender=User)
def new_user(sender, **kwargs):
    """
    Criamos um UserProfile quando  criamos um novo User.
    """
    if kwargs.get('created', False):
        userprofile = UserProfile()
        userprofile.user = kwargs.get("instance")
        userprofile.save()


@receiver(post_delete, sender=UserProfile)
def delete_userprofile(sender, **kwargs):
    """
    Eliminamos o usuario vinculado num userprofile.
    """
    userprofile = kwargs.get("instance")
    user = userprofile.user
    user.delete()
