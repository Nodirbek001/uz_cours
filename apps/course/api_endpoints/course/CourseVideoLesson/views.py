from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.course.api_endpoints.course.CourseVideoLesson.serializers import CourseVideoLessonListSerializer
from apps.course.models import VideoLesson, Chapter


class CourseVideoLessonAPIView(generics.RetrieveAPIView):
    serializer_class = CourseVideoLessonListSerializer
    queryset = VideoLesson.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CourseVideoLessonListSerializer(instance, context={'request': request})
        return Response(serializer)


    def get_object(self):
        return get_object_or_404(Chapter, pk=self.kwargs["chapter_id"])
