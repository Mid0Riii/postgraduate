"""postgraduate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework.documentation import include_docs_urls
from rest_framework.renderers import CoreJSONRenderer

urlpatterns = [
                  path('', admin.site.urls),
                  path("favicon.ico", RedirectView.as_view(url="static/favicon.ico")),
                  path('api/login/', obtain_jwt_token),
                  path('api/comm/', include("common.urls")),
                  path('api/award/', include("award.urls")),
                  path('api/basic/', include("basic.urls")),
                  path('api/semester/', include("semester.urls")),
                  path('api/auth/', include("myauth.urls")),
                  path('api/scholarship/', include("scholarship.urls")),
                  url(r'^docs/', include_docs_urls(title='API接口文档',
                                                   description="研究生管理系统后端API文档，后端返回标准格式{\n'code':'',\n'message':'',\n'data':''\n}\n")),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
