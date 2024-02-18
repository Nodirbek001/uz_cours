from django.urls import path

from apps.common import views

urlpatterns = [
    path('get/json', views.getJson.as_view()),
]