from django.urls import path, include

urlpatterns = [
    path("users/", include("apps.users.urls")),
    path("course/", include("apps.course.urls")),
    path('common/', include('apps.common.urls')),
]
