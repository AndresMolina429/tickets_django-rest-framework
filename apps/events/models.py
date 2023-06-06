from django.db import models
from ..locations.models import Locations

# Create your models here.

class Events(models.Model):
      date = models.DateTimeField('Fecha del evento', blank=False, null= False)
      locationId = models.ForeignKey(Locations, on_delete=models.PROTECT, db_column='location_id')
      name = models.CharField(max_length=50)
      description = models.CharField(max_length=200)
      created_at = models.DateTimeField(auto_now_add=True)
      
      class Meta:
            db_table = 'events'
            verbose_name = 'events'
            verbose_name_plural = 'events'

