from django.contrib import admin
from .models import DepartControl


class DepartureControlInline(admin.TabularInline):
    model = DepartControl
    extra = 1
    classes = ['collapse']
    # 显示跳转超链接
    show_change_link = True
