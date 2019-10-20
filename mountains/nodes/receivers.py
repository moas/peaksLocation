from django.utils.text import slugify
from django.contrib.gis.geos.point import Point


def slugify_name(sender, instance, **kwargs):
    instance.slug_name = slugify(instance.name)


def normalize_coordinates(sender, instance, **kwargs):
    lon, lat, alt = instance.coordinates.coords
    lon = float("%.6f" % lon)
    lat = float("%.6f" % lat)
    instance.coordinates = Point(lon, lat, alt)
