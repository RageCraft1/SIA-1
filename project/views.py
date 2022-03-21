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
        if user is not None:
            login(request,user)
            return redirect('lobbyView')
        else:   
            messages.info(request, 'Username or Password is incorrect!')
    context = {}
    return render(request, 'signin.html',context)

#Admin Sign in
def signin(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password')

        user = authenticate(username=username, password = password1)
        if user.is_staff:
              login(request,user)
              return redirect('adminLobby')
        else:   
            messages.info(request, 'Username or Password is incorrect!')
    context = {}
    return render(request, 'signin.html',context)

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

class dashboardView(View):   
    def get(self, request):
        if 'SearchBook' in request.GET:
            q1 = request.GET['q1']
            q2 = request.GET['q2']
            q3 = request.GET['q3']
            print(q3)
            # multiQ = Q(Q(employee_id__icontains=q) & Q(firstname__icontains=q) )

            if q1 and q2 != '':
                book = Book.objects.filter(date=q1).filter(resTime=q2)
                reservation = Reservation.objects.all()

            elif q1 and q3 != '':
                book = Book.objects.filter(date=q1).filter(title=q3)
                reservation = Reservation.objects.all()

            elif q2 and q3 != '':
                book = Book.objects.filter(resTime=q2).filter(title=q3)
                reservation = Reservation.objects.all()

            else:
                if q3 == '':
                    book = Book.objects.filter(resTime=q2) or Book.objects.filter(Q(date=q1))
                else:
                    book = Book.objects.filter(title=q3)
                reservation = Reservation.objects.all()
            # print(employee)
            # department = Department.objects.all()
            # designation = Designation.objects.all()
        else:
            reservation = Reservation.objects.all()
            #designation = Designation.objects.all()
            book = Book.objects.all()

        context = {
            'reservation': reservation,
            'book': book,
        }

        return render(request, 'dashboard.html', context)

    def post(self, request):
        if request.method == 'POST':
            if 'btnUpdate' in request.POST:
                print ('update profile button clicked')
                did=request.POST.get("book-Id")
                date=request.POST.get("d-date")
                startTime=request.POST.get("d-startTime")
                endTime=request.POST.get("d-endTime")
                title=request.POST.get("i-title")
                prefix=request.POST.get("d-prefix")
                firstname=request.POST.get("d-firstname")
                middlename=request.POST.get("d-middlename")
                lastname=request.POST.get("d-lastname")

                update_book = Book.objects.filter(id=did).update(date=date, startTime=startTime, 
                endTime=endTime, title=title, prefix=prefix, firstname=firstname, middlename=middlename, lastname=lastname)
                print(update_book)

                print('profile updated')
            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                did=request.POST.get("bbook-id")
                book=Book.objects.filter(id=did).delete()
                print('recorded deleted')

        return redirect('latest_reservation')

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

