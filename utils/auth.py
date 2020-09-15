from django.contrib.auth.backends import ModelBackend
from rest_framework.exceptions import APIException
from django.contrib.auth import get_user_model

User = get_user_model()


class MyBackend(ModelBackend):
    """
    自定义用户验证
    """

    def authenticate(self, request, username=None, password=None, **kwargs):  # 重写这个函数
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):  # 加密后比对前端密码
                return user
        except Exception as e:
            detail = "无此用户"
            # print(isinstance(detail,dict))
            # 异常信息UserProfile matching query does not exist
            raise APIException(detail=detail)
        else:
            detail = "用户名或密码错误"
            raise APIException(detail=detail)
