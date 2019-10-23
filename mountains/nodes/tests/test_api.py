import pytest

from django.apps import apps
from rest_framework.reverse import reverse

pytestmark = pytest.mark.django_db


def test_create_peak(api_client):
    response = api_client.post(
        reverse("api:peak-list"),
        {
            "name": "Mont Nimba",
            "latitude": 7.616667,
            "longitude": 8.416667,
            "altitude": 1752
        }
    )
    assert response.status_code == 201
    model = apps.get_model("nodes.Peak")
    peaks = model.objects.all()
    assert peaks.count() == 1
    peak = peaks.first()
    assert peak.name == "Mont Nimba"


def test_list_peak(api_client, peak, mont_blanc):
    response = api_client.get(reverse("api:peak-list"))
    assert response.status_code == 200
    features = response.data["features"]
    assert len(features) == 2


def test_read_peak(api_client, peak):
    response = api_client.get(reverse("api:peak-detail", args=(peak.pk, )))
    assert response.status_code == 200
    properties = response.data["properties"]
    assert properties["name"] == peak.name


def test_update_peak(api_client, mont_blanc):
    new = {
        "name": "Mont Nimba",
        "latitude": 7.616667,
        "longitude": 8.416667,
        "altitude": 1752
    }
    lon, lat, alt = mont_blanc.coordinates.coords
    assert mont_blanc.name != new["name"]
    assert lon != new["longitude"]
    assert lat != new["latitude"]
    assert alt != new["altitude"]

    api_client.put(reverse("api:peak-detail", args=(mont_blanc.pk, )), new)
    model = apps.get_model("nodes.Peak")
    obj = model.objects.get(pk=mont_blanc.pk)

    lon, lat, alt = obj.coordinates.coords
    assert obj.name == new["name"]
    assert lon == new["longitude"]
    assert lat == new["latitude"]
    assert alt == new["altitude"]


def test_delete_peak(api_client, peak):
    response = api_client.delete(reverse("api:peak-detail", args=(peak.pk, )))
    assert response.status_code == 204
    model = apps.get_model("nodes.Peak")
    assert model.objects.exists() is False


def test_search_ok_peak(api_client, mont_blanc):
    bbox = "-54.5247541978, 2.05338918702, 9.56001631027, 51.1485061713" # france
    response = api_client.get(f'{reverse("api:peak-list")}?in_bbox={bbox}')
    features = response.data["features"]
    assert len(features) == 1
    feature = features[0]
    assert mont_blanc.pk == feature["id"]


def test_search_nok_peak(api_client, mont_blanc):
    bbox = "8.79799563969, -3.97882659263, 14.4254557634, 2.32675751384"  # gabon
    response = api_client.get(f'{reverse("api:peak-list")}?in_bbox={bbox}')
    features = response.data["features"]
    assert len(features) == 0
