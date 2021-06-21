from django.urls import path
from . import views

urlpatterns = [
    path('',views.register,name="register"),
    path('fetchstudent/',views.fetchStudent,name="fetchStudent"),
    path('editstudent/',views.editStudent,name="fetchStudent"),

]
