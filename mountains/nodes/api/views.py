from rest_framework import viewsets

from ..models import Peak
from .serializers import PeakSerializer


class PeakViewSet(viewsets.ModelViewSet):
    """
    Manage Peak
    """
    serializer_class = PeakSerializer
    queryset = Peak.objects.all()
