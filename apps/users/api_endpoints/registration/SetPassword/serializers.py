from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class SetPasswordSerializer(serializers.Serializer):
    session = serializers.CharField(max_length=32)
    password = serializers.CharField(max_length=128, min_length=8, required=True)
    password_confirm = serializers.CharField(max_length=128, min_length=8, required=True)

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise ValidationError({"error": _("Passwords don't match")})
        return data
