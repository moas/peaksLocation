import pytest

from rest_framework.reverse import reverse

pytestmark = pytest.mark.django_db


def test_peak_api_urls():
    assert reverse("api:peak-list") == "/api/peaks/"
    assert reverse("api:peak-detail", args=(1, )) == "/api/peaks/1/"
    assert reverse("nodes:map-index") == "/map/"

