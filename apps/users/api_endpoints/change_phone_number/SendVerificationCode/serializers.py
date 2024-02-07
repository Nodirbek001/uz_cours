from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from apps.users.models import CustomUser


class SendVerificationCodeSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=8, max_length=128, required=True)
    new_phone_number = PhoneNumberField(required=True, region="UZ")

    class Meta:
        ref_name = "SendVerificationCodePhoneSerializer"

    def validate(self, data):
        user = self.context['request'].user
        password = data.get('password')
        if not user.check_password(password):
            raise ValidationError({"password": _("You password is incorrect.")})
        if CustomUser.objects.filter(phone_number=data["new_phone_number"]).exists():
            return serializers.ValidationError({"new_phone_number": _("This phone number is unvailable")})

        return data
