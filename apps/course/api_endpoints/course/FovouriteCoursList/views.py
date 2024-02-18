from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from apps.course.api_endpoints.course.FovouriteCoursList.serializers import FavouriteCourseSerializer
from apps.course.models import FavouriteCourse


class FavouriteCourseAPIListView(ListAPIView):
    serializer_class = FavouriteCourseSerializer
    queryset = FavouriteCourse.objects.all()
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend
    ]

    search_fields = ['course__title']
    filterset_fields = {'user': ['exact']}
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
