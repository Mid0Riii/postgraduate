from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics,permissions
from .serializers import AddressSerializers
from utils.drf import FormatResponse
from rest_framework.views import APIView,status
from .models import Student,StudentClass
# Create your views here.

User = get_user_model()

# class UserInfo()

class AddressBookList(generics.ListAPIView):
    def get_queryset(self):
        user = self.request.user
        userclass = Student.objects.get(stu_usr=user).stu_class
        return Student.objects.filter(stu_class=userclass)

    serializer_class = AddressSerializers
    permissions_classes = [permissions.IsAuthenticated]