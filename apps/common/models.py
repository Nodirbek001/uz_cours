from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created date"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated date"))

    class Meta:
        abstract = True


class text(models.Model):
    type = models.CharField(max_length=256, blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    date_unixtime = models.CharField(blank=True, null=True)
    from1 = models.CharField(blank=True)
    from_id = models.CharField(max_length=256, blank=True, null=True)
    forwarded_from = models.CharField(blank=True, null=True, max_length=256)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.from_id

    class Meta:
        verbose_name = _("Text")
        verbose_name_plural = _("Texts")


class text_entitys(models.Model):
    type = models.CharField(max_length=256, blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = _("text_entity")
        verbose_name_plural = _("text_entities")
