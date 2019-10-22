import unittest.mock as mock

import pytest

from django.conf import settings
from django.test import override_settings

from ..middleware import CountryGateAccess
from ..models import Report

pytestmark = pytest.mark.django_db

middleware = settings.MIDDLEWARE
middleware.insert(0, "mountains.gate.middleware.CountryGateAccess")


def forge_request(request_factory, ip):
    request = request_factory.request()
    request.META = {
        "HTTP_X_FORWARDED_FOR": ip,
        "REMOTE_ADDR": ip
    }
    request.path = "/"
    request.session = {}
    return request


def test_bad_ip_address(request_factory):
    request = forge_request(request_factory, 'fake')
    with override_settings(MIDDLEWARE=middleware):
        fn = CountryGateAccess()
        response = fn.process_request(request)
        assert response.status_code == 403


@mock.patch("mountains.gate.middleware.geocoder.ip")
def test_blacklisted_ip(mock_ip, request_factory):
    type(mock_ip.return_value).country = mock.PropertyMock(return_value="US")
    request = forge_request(request_factory, '127.0.0.1')
    with override_settings(MIDDLEWARE=middleware, GATE_WHITELIST_COUNTRIES=["FR"]):
        fn = CountryGateAccess()
        response = fn.process_request(request)
        assert response.status_code == 403

    reports = Report.objects.all()
    assert reports.count() == 1
    report = reports.first()
    assert report.ip == "127.0.0.1"
    assert report.origin == "US"


@mock.patch("mountains.gate.middleware.geocoder.ip")
def test_good_ip(mock_ip, request_factory):
    type(mock_ip.return_value).country = mock.PropertyMock(return_value="FR")
    request = forge_request(request_factory, '127.0.0.1')
    with override_settings(MIDDLEWARE=middleware, GATE_WHITELIST_COUNTRIES=["FR"]):
        fn = CountryGateAccess()
        response = fn.process_request(request)
        assert response is None

    reports = Report.objects.all()
    assert reports.count() == 0


def test_empty_whitelist(request_factory):
    request = forge_request(request_factory, '127.0.0.1')
    with override_settings(
        MIDDLEWARE=middleware,
        GATE_WHITELIST_COUNTRIES=[]
    ):
        fn = CountryGateAccess()
        response = fn.process_request(request)
        assert response is None

    reports = Report.objects.all()
    assert reports.count() == 0


def test_strict_mode(request_factory):
    request = forge_request(request_factory, '127.0.0.1')
    with override_settings(
        MIDDLEWARE=middleware,
        GATE_STRICT_MODE=True,
        GATE_WHITELIST_COUNTRIES=["FR"]
    ):
        fn = CountryGateAccess()
        response = fn.process_request(request)
        assert response.status_code == 403

    reports = Report.objects.all()
    assert reports.count() == 1
    report = reports.first()
    assert report.ip == "127.0.0.1"
    assert report.origin == ""


def test_no_strict_mode(request_factory):
    request = forge_request(request_factory, '127.0.0.1')
    with override_settings(
        MIDDLEWARE=middleware,
        GATE_STRICT_MODE=False,
        GATE_WHITELIST_COUNTRIES=["FR"]
    ):
        fn = CountryGateAccess()
        response = fn.process_request(request)
        assert response is None

    reports = Report.objects.all()
    assert reports.count() == 0
