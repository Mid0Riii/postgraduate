from django.urls import path,re_path
from django.conf.urls import include, url
from rest_framework import routers
from . import views

# routers = routers.DefaultRouter()
# routers.register(r'ann',views.AnnouncementList,basename='announcementlist')



urlpatterns=[
    path('ann',views.AnnouncementList.as_view()),
]