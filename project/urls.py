from xml.dom.minidom import Document
from django.urls import path
from .import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

app_name = 'project'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index, name="home"),

    #User Sign in and Out
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('logout',views.logOutUser,name ="logout_view"),

    #admin
    path('adminSide/', views.adminSide, name ="adminLobby"),
    path('addrooms/', views.addrooms, name = "addrooms"),

    #Basic functions
    path('protocol/',views.protocol),
    path('lobby/',views.lobbyView.as_view(),name="lobbyView"),
    path('rooms/',views.rooms),
    path('host-participant/',views.hostParticipant,name="host-participant"),

    #Participant forms
    path('participant-form/',views.participant,name="participant"), 
    path('participant-info/',views.participantInfo, name="participantInfo"),

    #Reservations or setup of rooms
    path('reservation/',views.reservationView.as_view(),name="reservationView"),
    path('room-setup/',views.roomsetup, name="roomsetup"),
    path('reservation-info/',views.reservedinfo, name="reservedinfo"),

    #Profile setup
    path('profile/',views.profile, name="profile"),
    path('edit-profile/',views.editProfile, name="edit-profile"),

    #settings
    path('settings/',views.settings, name="settings"),
    #deleteUser
    path('delete/',views.deleteUser, name="delete"),
    #dashboard
    path('dashboard/',views.dashboard, name="dashboard"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)