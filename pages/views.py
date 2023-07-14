from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="loginpage")
def profilepage(request):
    context={
        
    }
    return render(request,"profile.html",context)

@login_required(login_url="loginpage")
def assignmentspage(request):
    context={
        
    }
    return render(request,"assignment.html",context)

@login_required(login_url="loginpage")
def performancepage(request):
    context={
        
    }
    return render(request,"performance.html",context)

@login_required(login_url="loginpage")
def resultspage(request):
    context={
        
    }
    return render(request,"result.html",context)
    
@login_required(login_url="loginpage")
def labrecpage(request):
    context={
        
    }
    return render(request,"labrec.html",context)
