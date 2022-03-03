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

class reservationView(View):
    def get(self,request):
        return render(request, 'reservations/reservation.html')
        
    def post(self, request):
        form = ReservationForm(request.POST)
        availRooms=request.POST.get("availRooms")
        print(availRooms)
        title=request.POST.get("title")
        print(title)
        availTime=request.POST.get("availTime")
        print(availTime)

        if form.is_valid():
            availRooms=request.POST.get("availRooms")
            title=request.POST.get("title")
            availTime=request.POST.get("availTime")
    
        form=Reservation(availRooms=availRooms, title=title, 
                            availTime=availTime)
            
        form.save()

        return redirect('userlobbyView')

class lobbyView(View):
    def get(self, request):
        reservation = Reservation.objects.all()
        context = {
            'reservation': reservation
        }
        return render(request,'userlobby.html', context)

    def post(self, request):
        if request.method == 'POST':
            if 'btnUpdate' in request.POST:
                print ('update profile button clicked')
                rid=request.POST.get("r-resId")
                availRooms=request.POST.get("r-availRooms")
                title=request.POST.get("r-title")
                availTime=request.POST.get("r-availTime")
                update_Res = Reservation.objects.filter(resId=rid).update(availRooms=availRooms, title=title, availTime=availTime)
                print(update_Res)

            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                
                rid=request.POST.get("res-resId")
                res=Reservation.objects.filter(resId=rid).delete()
                print('recorded deleted')

        return redirect('lobbyView')

def protocol(request):
    return render(request, 'protocol.html')

def lobby(request):
    return render(request, 'userlobby.html')

def rooms(request):
    return render(request, 'rooms.html')

def hostParticipant(request):
    return render(request, 'hostParticipant.html')

def participant(request):
    return render(request, 'participant/participantForm.html')

def participantInfo(request):
    return render(request, 'participant/participantInfo.html')

#def reservation(request):
 #   return render(request, 'reservations/reservation.html')

def roomsetup(request):
    return render(request, 'reservations/roomsetup.html')

def reservedinfo(request):
    return render(request, 'reservations/reservedinfo.html')



def profile(request):
    return render(request, 'profile.html')

