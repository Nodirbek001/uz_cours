from rest_framework.serializers import ModelSerializer

from apps.course.models import Course, FavouriteCourse
from apps.users.models import CustomUser


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'author',
            'lang_code',
            'price',
            'discounted_price',
            'category',
            'level',
            'created_at',
            'updated_at'
        ]


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'is_staff',
            'is_superuser',
            'created_at',
            'updated_at'
        ]


class FavouriteCourseSerializer(ModelSerializer):
    class Meta:
        model = FavouriteCourse
        fields = [
            'id',
            'course',
            'user',
        ]
