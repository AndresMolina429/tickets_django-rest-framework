from django.db import models
from ..events.models import Events

# Create your models here.
class Tickets(models.Model):
      eventId = models.ForeignKey(Events, on_delete=models.PROTECT, db_column='event_id')
      created_at = models.DateTimeField(auto_now_add=True)

      class Meta:
            db_table = 'tickets'
            verbose_name = 'tickets'
            verbose_name_plural = 'tickets'