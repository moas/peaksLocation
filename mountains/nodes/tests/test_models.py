import pytest

from django.utils.text import slugify

from ..models import Peak

pytestmark = pytest.mark.django_db


def test_peak_slug(peak: Peak):
    assert peak.slug_name == slugify(peak.name)


def test_peak_str(peak: Peak):
    assert str(peak) == peak.name
