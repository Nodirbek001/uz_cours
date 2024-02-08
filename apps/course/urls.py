from django.urls import path

from apps.course.api_endpoints import course

urlpatterns = [
    # course list
    path('course_lists/', course.CourseListsAPIView.as_view(), name='course_lists')
]