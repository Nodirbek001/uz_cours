from rest_framework import permissions, filters
from rest_framework.generics import ListAPIView

from apps.course.api_endpoints.course.CourseLists.serializers import CourseCategorySerializer
from apps.course.models import CourseCategory


class CourseCategoryListApiView(ListAPIView):
    serializer_class = CourseCategorySerializer
    permission_classes = [permissions.AllowAny]
    search_fields = ['title']
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    queryset = CourseCategory.objects.all()

