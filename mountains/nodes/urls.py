from django.urls import path

from .views import MapView

app_name = "nodes"
urlpatterns = [
    path("", view=MapView.as_view(), name="map-index"),
]
