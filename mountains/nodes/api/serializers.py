from django.contrib.gis.geos import Point
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from ..models import Peak


class PeakSerializer(GeoFeatureModelSerializer):
    latitude = serializers.FloatField(write_only=True)
    longitude = serializers.FloatField(write_only=True)
    altitude = serializers.FloatField(write_only=True)

    class Meta:
        model = Peak
        geo_field = "coordinates"
        fields = ("id", "name", "latitude", "longitude", "altitude")

    def get_fields(self):
        fields = super().get_fields()
        fields["coordinates"].read_only = True
        return fields

    def validate(self, attrs):
        attrs = super().validate(attrs)
        point = Point(x=attrs["longitude"], y=attrs["latitude"], z=attrs["altitude"])
        attrs["coordinates"] = point
        for field in ("latitude", "longitude", "altitude"):
            attrs.pop(field, None)
        return attrs
