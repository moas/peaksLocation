import pytest

from ..models import Report

pytestmark = pytest.mark.django_db


def test_report_str(report: Report):
    assert str(report) == f"{report.ip} from {report.origin}"
