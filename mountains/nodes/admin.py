from django.contrib.gis import admin

from .models import Peak
# Register your models here.


@admin.register(Peak)
class PeakAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'latitude', 'longitude', 'altitude', 'created', 'modified')
    modifiable = False

    def latitude(self, obj):
        return obj.coordinates.coords[1]

    def longitude(self, obj):
        return obj.coordinates.coords[0]

    def altitude(self, obj):
        return obj.coordinates.coords[2]
