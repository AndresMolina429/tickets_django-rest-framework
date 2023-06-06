from rest_framework import serializers
from .models import LocationType, Locations

class LocationTypeSerializer(serializers.ModelSerializer):
      class Meta:
            model = LocationType
            fields = ('__all__')

class LocationSerializer(serializers.ModelSerializer):
      class Meta:
            model = Locations
            # fields = ('id', 'name','max_number_of_entries')
            fields = ('__all__')
            # read_only_fields = ('created_at)

