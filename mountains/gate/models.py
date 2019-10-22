from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel
# Create your models here.


class Report(TimeStampedModel):
    ip = models.GenericIPAddressField()
    origin = models.CharField(max_length=2, blank=True)

    class Meta:
        verbose_name = _("report")
        verbose_name_plural = _("Report ip blocked")

    def __str__(self):
        return f"{self.ip} from {self.origin}"
