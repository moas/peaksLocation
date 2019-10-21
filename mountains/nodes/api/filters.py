from django_filters import rest_framework as filters
from rest_framework_gis import filters

from ..models import Peak


class BboxFilter(filters.FilterSet):
    bbox = filters.CharFilter(method='search_in_bbox', help_text="format: xmin,xmax,ymin,ymax")

    class Meta:
        model = Peak
        fields = ("bbox", )

    def search_in_bbox(self, queryset, name, value):
        pass
