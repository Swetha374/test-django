"""user_management URL Configuration

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
from __future__ import annotations

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse
from django.urls import include
from django.urls import path
from django.urls import re_path as url
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView
from django.views.static import serve
from rest_framework.permissions import AllowAny
from rest_framework.schemas import get_schema_view


@require_http_methods(['GET'])
def home(request):
    return HttpResponse('<h1>Django is running, <br> Now you can customise this page </h1>')


urlpatterns = [
    url(r'^$',  home),
    path('api/admin/', admin.site.urls),
    path('api/user/', include('users.urls')),


    # path("api/video_subtitle/", include("video_subtitle.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )
