from .models import Locations, LocationType
from rest_framework import viewsets, permissions
from .serializers import LocationSerializer, LocationTypeSerializer

class LocationTypeViewSet(viewsets.ModelViewSet):
      queryset = LocationType.objects.all()
      permission_classes = [ permissions.AllowAny]
      serializer_class = LocationTypeSerializer

class LocationsViewSet(viewsets.ModelViewSet):
      queryset = Locations.objects.all()
      permission_classes = [ permissions.AllowAny]
      serializer_class = LocationSerializer