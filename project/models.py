from django.db import models

# Create your models here.
class Reservation(models.Model):
    resId = models.AutoField(primary_key = True)
    availRooms = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=50, null=True)
    resDate = models.DateField(null=True)
    resTime = models.TimeField(null=True)
    class meta:
        db_table='Reservation'
