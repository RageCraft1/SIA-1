from django.urls import path
from .import views
from django.contrib import admin

app_name = 'project'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),

    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('logout',views.logOutUser,name ="logout_view"),

    path('protocol/',views.protocol),
    path('lobby/',views.lobby,name="lobby"),
    path('rooms/',views.rooms),

    path('profile/',views.profile),
]