"""
URL configuration for uz_cours project.

The `urlpatterns` list routes URLs to views.py. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views.py
    1. Add an import:  from my_app import views.py
    2. Add a URL to urlpatterns:  path('', views.py.home, name='home')
Class-based views.py
    1. Add an import:  from other_app.views.py import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from uz_cours.schema import swagger_urlpatterns

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path('api/v1/', include('apps.v1')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += swagger_urlpatterns
urlpatterns += i18n_patterns(path("admin/", admin.site.urls))
if "rosetta" in settings.INSTALLED_APPS:
    urlpatterns +=[re_path(r'^rosetta/', include('rosetta.urls'))]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path("api-auth/", include("rest_framework.urls"))]