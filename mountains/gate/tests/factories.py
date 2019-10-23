from faker import Faker
from faker.providers import internet, address
from factory import DjangoModelFactory

from ..models import Report

fake = Faker()
fake.add_provider(internet)
fake.add_provider(address)


class ReportFactory(DjangoModelFactory):

    class Meta:
        model = Report

    ip = fake.ipv4()
    origin = fake.country_code(representation="alpha-2")
