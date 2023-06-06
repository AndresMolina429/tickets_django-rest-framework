from django.db import models
from ..tickets.models import Tickets

# Create your models here.
class People(models.Model):
      id = models.BigIntegerField('Identificacion persona', primary_key=True)
      ticketId = models.ForeignKey(Tickets, on_delete=models.PROTECT, db_column='ticket_id')

      class Meta:
            db_table = 'people'
            verbose_name = 'people'
            verbose_name_plural = 'people'
