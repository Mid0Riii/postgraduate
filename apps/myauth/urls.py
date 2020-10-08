from django.urls import path,re_path
from django.conf.urls import include, url
from rest_framework import routers
from . import views

urlpatterns=[
    path('',views.UserView.as_view())
]