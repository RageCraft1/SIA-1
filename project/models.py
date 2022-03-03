from django.db import models

# Create your models here.
class Reservation(models.Model):
    resId = models.AutoField(primary_key = True)
    availRooms = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=50, null=True)
    availTime = models.IntegerField()
    class meta:
        db_table='Reservation'
