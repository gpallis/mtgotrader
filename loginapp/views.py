from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

# Create your views here.
def loginattempt(request):
    if (request.POST): #attempted login
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if (user):
            login(request,user)
            return HttpResponseRedirect(reverse('loginapp.views.profile'))
        else:
            return loginpage(request,'Incorrect username or password. Please try again.')
    else:
        return loginpage(request,'') #login page accessed for the first time
        
def loginpage(request,message):
    return render(request,'login/loginform.html', {'msg':message})
    
@login_required
def profile(request):
    return HttpResponse('hello ' + request.user.username)
