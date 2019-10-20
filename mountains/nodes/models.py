from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

# Create your models here.


class Peak(TimeStampedModel):
    name = models.CharField(max_length=30)
    slug_name = models.SlugField(max_length=30, db_index=True, editable=False)
    coordinates = models.PointField(dim=3, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('peak')
        verbose_name_plural = _('Peaks')
