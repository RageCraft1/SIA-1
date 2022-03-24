from dataclasses import fields
from django.forms import ModelForm
from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('availRooms','title','resDate','resTime')

class UserDeleteForm(forms.ModelForm):
	class Meta:
		model = User
		fields= ('username',)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('availRooms', 'bRoom', 'numBook')

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('roomtype','image')


