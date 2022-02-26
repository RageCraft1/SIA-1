from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from matplotlib.style import context
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'index.html')

def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account was created')
            return render(request,'signin.html',{'articles':'signin'})
        else:
            messages.warning(request,'Username or Password is not valid!')
    context = {
        'form':form
    }
    return render(request,'signup.html',context)

  #  context = {'form':form}
   # return render(request, 'signup.html', context)

def signin(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password')

        user = authenticate(username=username, password = password1)
        if user is not None:
            login(request,user)
            return render(request, 'userlobby.html',{'article':'lobby'})
        else:
            messages.info(request, 'Username or Password is incorrect!')

    return render(request, 'signin.html')

def logOutUser(request):
	logout(request)
	return redirect('articles:sigin')


def protocol(request):
    return render(request, 'protocol.html')

def lobby(request):
    return render(request, 'userlobby.html')

def rooms(request):
    return render(request, 'rooms.html')

def profile(request):
    return render(request, 'profile.html')

