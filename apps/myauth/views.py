# -*- coding:utf-8 -*-
from .models import CustomUser
from rest_framework_jwt.utils import jwt_decode_handler
from .serializers import CustomUserSerializers
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.contrib.auth.backends import ModelBackend
from rest_framework.exceptions import APIException
from utils.drf import FormatResponse


class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """

    def authenticate(self, request, username=None, password=None, **kwargs):  # 重写这个函数
        try:
            user = CustomUser.objects.get(username=username)
            if user.check_password(password):  # 加密后比对前端密码
                return user
        except Exception as e:
            detail = "无此用户"
            # print(isinstance(detail,dict))
            # 异常信息UserProfile matching query does not exist
            raise APIException(detail=detail)
        else:
            detail = "无此用户"
            raise APIException(detail=detail)


class UserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        usr = CustomUser.objects.get(id=request.user.id)
        s = CustomUserSerializers(instance=usr)
        data = s.data
        data["password"]=""
        return FormatResponse(data=data, msg="获取成功", code=200, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            data = request.data
            new_pwd = data["password"]
            usr = CustomUser.objects.get(id=request.user.id)
            usr.set_password(new_pwd)
            usr.save()
            return FormatResponse(data=data, msg="修改成功", code=200, status=status.HTTP_200_OK)
        except Exception as e:
            return FormatResponse(data=e, msg="修改失败", code=400, status=status.HTTP_400_BAD_REQUEST)
