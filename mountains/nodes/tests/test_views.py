import pytest

from django.apps import apps
from django.urls import reverse
from django.core.serializers import serialize

pytestmark = pytest.mark.django_db


def test_map_view(test_client):
    response = test_client.get(reverse("nodes:map-index"))
    model = apps.get_model("nodes.peak")
    assert response.status_code == 200
    assert response.template_name == ['nodes/map.html']
    assert response.context["nodes"] == serialize('geojson', model.objects.all(),
                                                  geometry_field="coordinates", fields=("name", ))
