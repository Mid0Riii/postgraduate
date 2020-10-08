from django.urls import path, re_path
from django.conf.urls import include, url
from rest_framework import routers
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'thesis', views.ThesisViewset, basename="thesis")
router.register(r'patent', views.PatentListViewsets, basename="patent")
router.register(r'scholarship', views.ScholarshipViewset, basename="scholarship")
router.register(r'prize', views.PrizeViewset, basename="prize")
router.register(r'fund', views.FundViewset, basename="fund")
router.register(r'honor', views.HonorViewset, basename="honor")

urlpatterns = [
    path('', include(router.urls)),
]
