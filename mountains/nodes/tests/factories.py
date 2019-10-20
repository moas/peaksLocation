import factory

from faker import Faker
from faker.providers import geo
from factory import DjangoModelFactory, fuzzy
from django.contrib.gis.geos.point import Point

from ..models import Peak


class PeakFactory(DjangoModelFactory):

    class Meta:
        model = Peak
        exclude = ("lat", "lon", "alt", "fake", "srid")

    fake = Faker()
    fake.add_provider(geo)

    lat = float(fake.latitude())
    lon = float(fake.longitude())
    alt = fuzzy.FuzzyFloat(1000, 5000)
    srid = 4326

    name = fake.name()
    coordinates = factory.LazyAttribute(lambda o: Point(o.lon, o.lat, o.alt, srid=o.srid))
