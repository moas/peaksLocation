import pytest
from django.conf import settings
from django.test import RequestFactory, Client
from rest_framework.test import APIClient

from mountains.users.tests.factories import UserFactory
from mountains.nodes.tests.factories import PeakFactory
from mountains.gate.tests.factories import ReportFactory


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
def mont_blanc() -> PeakFactory:
    return PeakFactory(
        name="Mont Blanc",
        lat=45.832622,
        lon=6.865175,
        alt=4810
    )


@pytest.fixture
def request_factory() -> RequestFactory:
    return RequestFactory()


@pytest.fixture
def test_client() -> Client:
    return Client()


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture
def report() -> ReportFactory:
    return ReportFactory()
