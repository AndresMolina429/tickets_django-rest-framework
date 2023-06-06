from rest_framework import routers
from .logic import LocationsViewSet, LocationTypeViewSet

router = routers.DefaultRouter()

router.register('location', LocationsViewSet,'locations')
router.register('location_type', LocationTypeViewSet,'locations_type')

urlpatterns = router.urls