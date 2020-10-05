from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics,permissions
from .serializers import ScoreSerializers,DepartureSerializers
from utils.drf import FormatResponse
from rest_framework.views import APIView,status
from .models import Score
from basic.models import Student
# Create your views here.

User = get_user_model()


class ScoreList(generics.ListAPIView):
    def get_queryset(self):
        user = self.request.user
        stu = Student.objects.get(stu_usr=user)
        return Score.objects.filter(sco_stu=stu)
    serializer_class = ScoreSerializers
    permissions_classes = [permissions.IsAuthenticated]

# class DepartureView(generics.ListAPIView,)