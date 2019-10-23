from django.contrib import admin
from .models import UserProfile, Login_Customer, Login_Partner


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'image_profile')

@admin.register(Login_Customer)
class Login_Customer(admin.ModelAdmin):
    list_display = ('sname' , 'semail','scontrasenia', 'bis_active', 'dtimestamp')

@admin.register(Login_Partner)
class Login_Partner(admin.ModelAdmin):
    list_display = ('sname' , 'semail','scontrasenia', 'bis_active', 'dtimestamp')