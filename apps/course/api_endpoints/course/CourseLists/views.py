from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from apps.course.api_endpoints.course.CourseLists.serializers import CourseListSerializer
from apps.course.models import Course


class CourseListsAPIView(ListAPIView):
    serializer_class = CourseListSerializer
    queryset = Course.objects.all()

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    search_fields = ['title', ]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


__all__ = ['CourseListsAPIView']
