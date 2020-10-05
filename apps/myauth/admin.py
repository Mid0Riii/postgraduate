from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    search_fields = ['username']
    list_display = ['username']
    list_filter = ['username']
