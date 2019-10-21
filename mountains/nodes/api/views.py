import coreapi
import coreschema

from rest_framework import viewsets
from rest_framework_gis.filters import InBBoxFilter

from ..models import Peak
from .serializers import PeakSerializer


class SearchFilterBackend(InBBoxFilter):
    def get_schema_fields(self, view):
        return [
            coreapi.Field(
                name='in_bbox',
                location='query',
                required=False,
                schema=coreschema.String(),
            )
        ]


class PeakViewSet(viewsets.ModelViewSet):
    """
    Manage Peak
    """
    serializer_class = PeakSerializer
    queryset = Peak.objects.all()
    bbox_filter_field = 'coordinates'
    filter_backends = (SearchFilterBackend, )
    bbox_filter_include_overlapping = True
