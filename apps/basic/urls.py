from django.urls import path, re_path
from django.conf.urls import include, url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'addressbook', views.AddressBookViewset, basename="addressbook")
router.register(r'poverty', views.PovertyViewset, basename="poverty")

urlpatterns = [
    path('', include(router.urls)),
]
