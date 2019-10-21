from django.views.generic import TemplateView
from django.core.serializers import serialize
from .models import Peak
# Create your views here.


class MapView(TemplateView):
    template_name = "nodes/map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nodes"] = serialize('geojson', Peak.objects.all(), geometry_field="coordinates", fields=("name", ))
        return context
