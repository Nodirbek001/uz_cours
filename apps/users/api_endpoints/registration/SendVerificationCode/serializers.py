from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from apps.users.choices import VIA_PHONE_NUMBER, VIA_EMAIL
from apps.users.models import CustomUser


class SendVerificationCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "full_name",
            "phone_number",
            "email",
        )
        ref_name = "SendVerificationCodeRegistrationSerializer"

    def validate(self, data):
        phone_number = data.get("phone_number", None)
        email = data.get("email", None)

        if phone_number is not None:
            if email is not None:
                raise ValidationError(
                    {
                        "error": _("You can enter only one of phone number and email at a time!")
                    }
                )
            if not CustomUser.is_phone_number_available(phone_number):
                raise ValidationError({"phone_number": _("This number is already taken")})
            data.update({"auth_type": VIA_PHONE_NUMBER})
            return data
        if email is not None:
            if not CustomUser.is_email_available(email):
                raise ValidationError({"email": _("This email is already taken")})
            data.update({"auth_type": VIA_EMAIL})
            return data
        raise ValidationError(
            {"error": _("You must enter phone number or email")}
        )
