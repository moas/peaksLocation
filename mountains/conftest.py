import pytest
from django.conf import settings
from django.test import RequestFactory
from rest_framework.test import APIClient

from mountains.users.tests.factories import UserFactory
from mountains.nodes.tests.factories import PeakFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> settings.AUTH_USER_MODEL:
    return UserFactory()


@pytest.fixture
def peak() -> PeakFactory:
    return PeakFactory()


@pytest.fixture
def request_factory() -> RequestFactory:
    return RequestFactory()


@pytest.fixture
def api_client():
    return APIClient()
