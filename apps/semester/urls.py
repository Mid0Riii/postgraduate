from django.urls import path, re_path
from django.conf.urls import include, url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'list', views.SemesterViewset, basename="Semester")
router.register(r'score', views.ScoreViewset, basename="Score")
router.register(r'departure', views.DepartureViewset, basename="Departure")

urlpatterns = [
    path('', include(router.urls)),
    # path('old',views.DepartureView.as_view())
]
