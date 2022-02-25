from django.urls import path
from .import views

app_name = 'project'

urlpatterns = [
    path('', views.index),
    path('signin/', views.signin),
    path('signup/', views.signup),
    path('protocol/',views.protocol),
    path('lobby/',views.lobby),
    path('rooms/',views.rooms),
]