from django.urls import path, re_path
from django.conf.urls import include, url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'ann', views.AnnouncementViewset, basename="announcement")

urlpatterns = [
    path('', include(router.urls)),
]
