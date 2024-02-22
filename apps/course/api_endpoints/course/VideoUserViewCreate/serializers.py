from rest_framework.serializers import ModelSerializer

from apps.course.models import VideoUserView


class VideoUserViewCreateSerializer(ModelSerializer):
    class Meta:
        model = VideoUserView
        fields = [
            'id',
            'video',
            'user',
            'is_finished'
        ]
