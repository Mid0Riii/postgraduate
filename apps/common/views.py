from django.shortcuts import render
from .serializers import AnnouncementSerializers
from rest_framework import mixins
from rest_framework import generics,permissions
from .models import Announcement


class AnnouncementList(generics.ListAPIView):
    queryset = Announcement.objects.filter(ann_visibility=True).order_by('ann_urgency')
    serializer_class = AnnouncementSerializers
    permission_classes = [permissions.IsAuthenticated]
