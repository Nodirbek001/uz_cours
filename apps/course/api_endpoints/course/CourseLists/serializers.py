from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.course.models import CourseCategory, Course


class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ['id', 'title', 'icon']


class CourseListSerializer(serializers.ModelSerializer):
    category = CourseCategorySerializer(read_only=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "author",
            "lang_code",
            "price",
            "discounted_price",
            "category",
            "level"
        ]
