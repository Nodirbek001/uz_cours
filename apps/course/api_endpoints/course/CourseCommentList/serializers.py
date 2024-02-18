from rest_framework import serializers

from apps.course.models import CourseComment
from apps.users.models import CustomUser


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'full_name', 'profile_pic'
        ]


class CourseCommentListSerializer(serializers.ModelSerializer):
    author = UserShortSerializer(read_only=True)

    class Meta:
        model = CourseComment
        fields = ['id', 'author', 'rating', 'comment_text', 'created_at']
