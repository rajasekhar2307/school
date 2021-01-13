from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name ="index"),
    path('home', views.home,name ="home"),
    path('slogin',views.slogin,name="slogin"),
    path('tlogin',views.tlogin,name="tlogin"),
    path('tlogout',views.tlogout,name="tlogout"),
]
