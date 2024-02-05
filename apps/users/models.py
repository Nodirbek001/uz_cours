from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework.authtoken.models import Token
from sorl.thumbnail.fields import ImageField

from apps.common.models import TimeStampedModel
from django.utils.translation import gettext as _

from apps.users.choices import AUTH_TYPES


# Create your models here.
class CustomUser(AbstractUser, TimeStampedModel):
    first_name = None
    last_name = None
    full_name = models.CharField(max_length=255, verbose_name=_('Full Name'), blank=True)
    profile_pic = ImageField(null=True, blank=True, upload_to='images/profile_pics/%Y/%m/%d/')
    birth_date = models.DateField(null=True, blank=True, verbose_name=_("Birth Date"))
    email = models.EmailField(verbose_name=_("Email"), null=True, blank=True)
    phone_number = PhoneNumberField(region='UZ', verbose_name=_("phone number"), null=True, blank=True)
    auth_type = models.CharField(max_length=30, choices=AUTH_TYPES)

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.username

    def get_tokens(self):
        token, created = Token.objects.get_or_create(user=self)
        data = {
            "token": token.key
        }
        return data

    @classmethod
    def is_phone_number_available(cls, phone_number):
        if cls.objects.filter(phone_number=phone_number).exists():
            return False
        return True

    @classmethod
    def is_email_available(cls, email):
        if CustomUser.objects.filter(email=email).exists():
            return False
        return True
