from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, viewsets,decorators
from .serializers import ScoreSerializers, SemesterSerializers, DepartureSerializers
from utils.drf import FormatResponse
from rest_framework.views import APIView, status
from basic.models import Student
from .models import Semester, Departure,Score
from utils.mixins import FormatListModelMixin, SafeFormatCreateModelMixin
from utils.permissions import IsOwnerOrReadOnly

# Create your views here.

User = get_user_model()


class SemesterViewset(viewsets.GenericViewSet, FormatListModelMixin):
    def get_queryset(self):
        return Semester.objects.filter(sem_is_available=True)

    serializer_class = SemesterSerializers
    permission_classes = [permissions.IsAuthenticated]


class DepartureViewset(viewsets.GenericViewSet, FormatListModelMixin, SafeFormatCreateModelMixin):
    def get_queryset(self):
        return Departure.objects.filter(depart_stu__stu_usr=self.request.user.id)

    serializer_class = DepartureSerializers
    permissions = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    auth_field_name = "depart_stu"


class ScoreViewset(viewsets.GenericViewSet,FormatListModelMixin):
    def get_queryset(self):
        return Score.objects.filter(sco_stu__stu_usr=self.request.user.id)
    serializer_class = ScoreSerializers
    permission_classes = [permissions.IsAuthenticated]



# class DepartureView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get(self, request):
#         sem = Semester.objects.get(sem_is_available=True)
#         s = SemesterSerializers(instance=sem)
#         sd = DepartureSerializers(instance=None)
#         data = {}
#         data["sem_info"] = s.data
#         data["dep_info"] = sd.data
#         return FormatResponse(data=data, code=200, msg="获取成功", status=status.HTTP_200_OK)
#
#     def post(self, request):
#         data = request.data
#         dep_info = data["dep_info"]
#         dep_info["depart_stu"] = Student.objects.get(stu_usr=request.user.id).id
#         sem = Semester.objects.get(sem_is_available=True)
#         sem_type = sem.sem_dep_status
#         dep_info["depart_type"] = sem_type
#         dep_info["depart_semster"] = sem.id
#         s = DepartureSerializers(data=dep_info)
#         if s.is_valid():
#             s.save()
#             return FormatResponse(data="", code=200, msg="提交成功", status=status.HTTP_201_CREATED)
#         else:
#             print(s.errors)
#             return FormatResponse(data=s.errors, code=400, msg="错误", status=status.HTTP_400_BAD_REQUEST)
