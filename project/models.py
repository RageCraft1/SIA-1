from distutils.command.upload import upload
import email
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Reservation(models.Model):
    resId = models.AutoField(primary_key = True)
    availRooms = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=50, null=True)
    resDate = models.CharField(max_length=50, null=True)
    resTime = models.CharField(max_length=50, null=True)
    class meta:
        db_table='Reservation'

class Book(models.Model):
    bookId = models.AutoField(primary_key = True)
    availRooms = models.ForeignKey(Reservation, on_delete=models.CASCADE, null=True)
    bRoom = models.IntegerField()
    numBook = models.IntegerField()
    class meta:
        db_table="Book"

class Room(models.Model):
    roomId = models.AutoField(primary_key = True)
    roomtype = models.CharField(max_length=50, null=True)
    image = models.ImageField(null = True, blank = True, upload_to="images/")
    
    ROOM_STATUS = ( 
    ("1", "available"), 
    ("2", "not available"),    
    ) 
    class meta:
        db_table="Room"

class Profile(models.Model):
    userId = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    lastname = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    phone_number = models.IntegerField()
    profpic = models.ImageField(null=True, blank=True, upload_to="images/")
    street = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    about =models.TextField(blank=True, null=True)
    class meta:
        db_table ="Profile"