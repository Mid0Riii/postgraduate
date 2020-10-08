from .drf import FormatResponse
from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.settings import api_settings


class SafeFormatCreateModelMixin:
    """
    解决create时可能出现的安全问题，需要在ApiView或Viewset内通过auth_field_name指定用户模型的主键或外键键名
    """

    def create(self, request, *args, **kwargs):
        auth = self.auth_field_name
        data = request.data.copy()
        data[auth] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return FormatResponse(code=201, msg="创建成功", data=serializer.data, status=status.HTTP_201_CREATED,
                              headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}


class FormatListModelMixin:
    """
    格式化ListModelMixin
    """

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return FormatResponse(code=200, msg="获取成功", data=serializer.data, status=status.HTTP_200_OK)


class FormatRetrieveModelMixin:
    """
    格式化RetrieveModelMixin
    """

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return FormatResponse(code=200, msg="获取成功", data=serializer.data, status=status.HTTP_200_OK)


class FormatUpdateModelMixin:
    """
    格式化UpdateModelMixin
    """

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return FormatResponse(code=201, msg="修改成功", data=serializer.data, status=status.HTTP_200_OK)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

class FormatDestroyModelMixin:
    """
    格式化Format
    """
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

