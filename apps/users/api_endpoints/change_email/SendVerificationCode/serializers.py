from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.users.models import CustomUser


class SendVerificationCodeSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=8, max_length=124, required=True)
    new_email = serializers.EmailField(required=True)

    class Meta:
        ref_name = "SendVerificationCodeEmailSerializer"

    def validate(self, data):
        user = self.context['request'].user
        password = data['password']
        if not user.check_password(password):
            raise ValidationError({"password": _("Your password is incorrect.")})
        if CustomUser.objects.filter(email=data['new_email']).exists():
            return ValidationError({"new_email": _("This email is unavailable")})
        return data
