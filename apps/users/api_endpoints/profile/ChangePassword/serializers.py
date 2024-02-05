from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(min_length=8, max_length=128, required=True)
    new_password = serializers.CharField(min_length=8, max_length=128, required=True)
    new_password_confirm = serializers.CharField(min_length=8, max_length=128, required=True)

    def validate(self, data):
        user = self.context['request'].user
        password = data["old_password"]
        if not user.check_password(password):
            raise ValidationError({"error": _("You password is incorrect")})
        if data["new_password"] != data["new_password_confirm"]:
            raise ValidationError({"error": _("You password does not match")})
        return data
