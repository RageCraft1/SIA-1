from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'index.html')

def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'signup.html', context)

def signin(request):
    return render(request, 'signin.html')

def protocol(request):
    return render(request, 'protocol.html')

def lobby(request):
    return render(request, 'userlobby.html')

def rooms(request):
    return render(request, 'rooms.html')

def profile(request):
    return render(request, 'profile.html')

