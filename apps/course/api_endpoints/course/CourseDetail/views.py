from rest_framework import generics
from rest_framework.views import APIView

from apps.course.api_endpoints.course.CourseDetail.serializers import CourseDetailSerializer
from apps.course.models import Course


class CourseDetailAPIView(generics.RetrieveAPIView):
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()


__all__ = ['CourseDetailAPIView']
