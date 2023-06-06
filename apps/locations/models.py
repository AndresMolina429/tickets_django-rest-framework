from django.db import models

# Create your models here.
class LocationType(models.Model):
      name = models.CharField('Tipo de Lugar(Teatro, estadio, salón de eventos, etc)',max_length=20)
      class Meta:
            db_table = 'location_type'
            verbose_name = 'location_type'
            verbose_name_plural = 'location_type'

class Locations(models.Model):
      locationTypeId = models.ForeignKey(LocationType, on_delete=models.PROTECT, db_column='location_type_id')
      name = models.CharField('Nombre del lugar de eventos',max_length=50, blank=False, null= False)
      max_number_of_entries= models.IntegerField('Cantidad Maximas de entradas', null=False)

      class Meta:
            db_table = 'locations'
            verbose_name = 'locations'
            verbose_name_plural = 'locations'
