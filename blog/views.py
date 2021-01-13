from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib import messages

# Create your views here.
def index(request):
	return render(request, 'blog/index.html')

def slogin(request):

    return render(request,'blog/slogin.html')

def tlogin(request):
    if(request.method=='POST'):
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username,password=password)
        if user is not None:
            auth.login(request,user)
            context = {'functions':[{'name':"Register Student",'desc':"Register a new student"},{'name':"Edit Student",'desc':"Edit student details"},{'name':"Student Marks",'desc':"Add/Remove Student Marks"},{'name':"Schedule",'desc':"View your schedule"}]}
            return redirect("/home")
        else:
            system_messages = messages.get_messages(request)
            for message in system_messages:
                # This iteration is necessary
                pass
            messages.info(request,"invalid credentials")
            return redirect("tlogin")
    else:
        return render(request,'blog/tlogin.html')

def tlogout(request):
    auth.logout(request)
    return redirect("/")
def home(request):
    context = {'functions':[{'name':"Register Student",'desc':"Register a new student",'link':"register"},{'name':"Edit Student",'desc':"Edit student details",'link':"edit/fetchstudent"},{'name':"Student Marks",'desc':"Add/Remove Student Marks",'link':"register"},{'name':"Schedule",'desc':"View your schedule",'link':"register"}]}
    return render(request,"blog/home.html",context)
