from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created date"))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated date"))

    class Meta:
        abstract = True
