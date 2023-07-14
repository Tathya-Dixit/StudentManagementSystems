from django.shortcuts import render,redirect
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages



def loginPage(request):
    if request.method=="GET":
        if request.user.is_authenticated:
            return redirect('profilepage')
        else:
            return render(request,'login.html',{})
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password = password)
        if user:
            login(request,user)
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group == 'student':
                return redirect('profilepage')
            if group == 'teacher':
                return redirect('profilepage')
            else:
                return redirect("loginpage")
        else:
            messages.info(request,"Username or Password Incorrect ! ") 
            return redirect("loginpage")


def logOut(request):
    logout(request)
    return redirect("loginpage")