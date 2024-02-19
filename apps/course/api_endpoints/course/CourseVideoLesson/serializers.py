from rest_framework import serializers

from apps.course.models import Chapter, VideoUserView, VideoLesson


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = [
            'id',
            'title'
        ]


class CourseVideoLessonShortSerializer(serializers.ModelSerializer):
    is_viewed = serializers.SerializerMethodField()

    def get_is_viewed(self, obj):
        if VideoUserView.objects.filter(user=self.context['request'].user, video=obj, is_finished=True).exists():
            return True
        else:
            return False

    class Meta:
        model = VideoLesson
        fields = ['id', 'title', 'video_path', 'video_thumbnail', 'is_viewed']


class CourseVideoLessonListSerializer(serializers.ModelSerializer):
    chapter = ChapterSerializer()
    lessons = serializers.SerializerMethodField()

    class Meta:
        model = VideoLesson
        fields = ['id', 'title', 'chapter', 'video_duration', 'video_path', 'lessons', 'video_thumbnail', ]

    def get_lessons(self, obj):
        print(self.context['request'])
        videos = obj.chapter.chapter.all()
        serializer = CourseVideoLessonShortSerializer(videos, many=True, context={"request": self.context['request']})
        return serializer.data
