from rest_framework import serializers

from apps.users.models import CustomUser


class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "full_name",
            "profile_pic",
            "birth_date",
        )
