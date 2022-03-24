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
from .models import Room
from .forms import RoomForm

#Brings User to the landing page
def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')
    
#Signs up user by creating a superuser without admin previledge
def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account was created')
            return redirect('signin')
        else:
            messages.warning(request,'Username or Password is not valid!')
    context = {
        'form':form
    }
    return render(request,'signup.html',context)

  #  context = {'form':form}
   # return render(request, 'signup.html', context)

#Signs in User
def signin(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password')

        user = authenticate(username=username, password = password1)
        if user.is_active:
            login(request,user)
            return redirect('lobbyView')
        if user.is_staff:
            login(request,user)
        else:   
            messages.info(request, 'Username or Password is incorrect!')
    context = {}
    return render(request, 'signin.html',context)


#Admin Sign in
#def signin(request):
#    if request.method =='POST':
#       username = request.POST.get('username')
#       password1 = request.POST.get('password')

#        user = authenticate(username=username, password = password1)
#        if user.is_staff:
#              login(request,user)
#              return redirect('adminLobby')
#        else:   
#            messages.info(request, 'Username or Password is incorrect!')
#    context = {}
#    return render(request, 'signin.html',context)

#Logs User Out
def logOutUser(request):
	logout(request)
	return redirect('articles:signin')


#Add a reservation for a room
class reservationView(View):
    def get(self,request):
        return render(request, 'reservations/reservation.html')
        
    def post(self, request):
        form = ReservationForm(request.POST)
        availRooms=request.POST.get("availRooms")
        print(availRooms)
        title=request.POST.get("title")
        print(title)
        resDate=request.POST.get("resDate")
        print(resDate)
        resTime=request.POST.get("resTime")
        print(resTime)

        if form.is_valid():
            availRooms=request.POST.get("availRooms")
            title=request.POST.get("title")
            resDate=request.POST.get("resDate")
            resTime=request.POST.get("resTime")
    
        form=Reservation(availRooms=availRooms, title=title, resDate=resDate, resTime=resTime)
            
        form.save()

        return redirect('lobbyView')

class addRoomView(View):
    def get(self,request):
        return render(request, 'addrooms.html')
        
    def post(self, request):
        form = RoomForm(request.POST)
        roomtype=request.POST.get("roomtype")
        print(roomtype)

        if form.is_valid():
            roomtype=request.POST.get("roomtype")
            
    
        form=Room(roomtype=roomtype)
            
        form.save()

        return redirect('roomView')

class roomView(View):
    def get(self,request):
        room = Room.objects.all()
        context = {
            'room': room
        }
        return render(request,'rooms.html', context)
        
    def post(self, request):
        if request.method == 'POST':
            if 'btnUpdate' in request.POST:
                print ('update profile button clicked')
                rtId=request.POST.get("rt-roomId")
                roomtype=request.POST.get("rt-roomtype")
                image=request.POST.get("rt-image")
                update_image = Room.objects.filter(roomId=rtId).update(roomtype=roomtype)
                print(update_image)
                print('profile updated')

            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                rtId=request.POST.get("room-id")
                image=Room.objects.filter(roomId=rtId).delete()
                print('recorded deleted')

        return redirect('roomView')

#Brings user to the homepage where he can locate most functions
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
                resDate=request.POST.get("r-resDate")
                resTime=request.POST.get("r-resTime")
                update_Res = Reservation.objects.filter(resId=rid).update(availRooms=availRooms, title=title, resDate=resDate, resTime=resTime)
                print(update_Res)

            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                
                rid=request.POST.get("res-resId")
                res=Reservation.objects.filter(resId=rid).delete()
                print('recorded deleted')

        return redirect('lobbyView')


#Edit Profile
class editProfile(View):
    def get(self,request):
        return render(request, 'updateProfile.html')
        
    def post(self, request):
        form = ProfileForm(request.POST)
        lastname=request.POST.get("lastname")
        print(lastname)
        email=request.POST.get("email")
        print(email)
        phone_number=request.POST.get("phone_number")
        print(phone_number)
        street=request.POST.get("street")
        print(street)
        city=request.POST.get("city")
        print(city)

        if form.is_valid():
            lastname=request.POST.get("lastname")
            email=request.POST.get("email")
            phone_number=request.POST.get("phone_number")
            street=request.POST.get("street")
            city=request.POST.get("city")
    
        form=Profile(lastname=lastname, email=email, phone_number=phone_number,street=street,city=city)
            
        form.save()

        return redirect('profile')

class profile(View):
    def get(self, request):
        profile = Profile.objects.all()
        context = {
            'profile': profile
        }
        return render(request,'profile.html', context)

    def post(self, request):
        if request.method == 'POST':
            if 'btnUpdate' in request.POST:
                print ('update profile button clicked')
                user = request.POST.get("p-userId")
                lastname=request.POST.get("p-lastname")
                email=request.POST.get("p-email")
                phone_number=request.POST.get("p-phone_number")
                street=request.POST.get("p-street")
                city=request.POST.get("p-city")
                update_Profile = Profile.objects.filter(userId=user).update(users=user,lastname=lastname, email=email, phone_number=phone_number,
                street=street,city=city)
                print(update_Profile)

            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                
                user=request.POST.get("p-userId")
                prof=Profile.objects.filter(userId=user).delete()
                print('recorded deleted')

        return redirect('profile')
        
def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'addrooms.html', {'form': form, 'img_obj': img_obj})
    else:
        form = RoomForm()
    return render(request, 'addrooms.html', {'form': form})

#Brings user to the protocol submit page
def protocol(request):
    return render(request, 'protocol.html')

#SOME EXTRA COPY OF LOBBY
def lobby(request):
    return render(request, 'userlobby.html')


def rooms(request):
    return render(request, 'rooms.html')

def adminSide(request):
    return render(request, 'adminLobby.html')

def addrooms(request):
    return render(request, 'addrooms.html')

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
    return render(request, 'profilenew.html')

def editProfile(request):
    return render(request, 'updateProfile.html' )

#Delete a User
def deleteUser(request):
	if request.method =='POST':
		delete_form = UserDeleteForm(request.POST, instance=request.user)
		user = request.user
		user.delete()

		messages.success(request,'User deleted successfuly')
		return redirect('home')

	else:
		delete_form = UserDeleteForm(instance=request.user)
	context= {
		'delete_form':delete_form
	}
	return render(request,'deleteacc.html',context)


def settings(request):
    return render(request, 'settings.html')

