from rest_framework.routers import DefaultRouter

from .views import PeakViewSet

router = DefaultRouter()
router.register("peaks", PeakViewSet, basename="peak")
urlpatterns = router.urls
