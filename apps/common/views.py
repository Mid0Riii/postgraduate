from .serializers import AnnouncementSerializers
from rest_framework import generics, permissions, viewsets
from .models import Announcement
from utils.mixins import FormatListModelMixin, FormatRetrieveModelMixin


class AnnouncementViewset(viewsets.GenericViewSet, FormatRetrieveModelMixin, FormatListModelMixin):
    """
    list:获取当前有效公告
    read:获取公告详情
    """
    queryset = Announcement.objects.filter(ann_visibility=True).order_by('ann_urgency')
    serializer_class = AnnouncementSerializers
    permission_classes = [permissions.IsAuthenticated]
