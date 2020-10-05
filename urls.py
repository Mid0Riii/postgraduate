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
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token

urlpatterns = [
    path('', admin.site.urls),
    path("favicon.ico",RedirectView.as_view(url="static/favicon.ico")),
    path('api/login/',obtain_jwt_token),
    path('api/comm/',include("common.urls")),
    path('api/basic/',include("basic.urls")),
    path('api/semester/',include("semester.urls")),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
