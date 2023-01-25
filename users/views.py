from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'website/home.html')

def register(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        my_user=User.objects.filter(username=uname)
        if my_user.exists():
            messages.warning(request,"Email is already taken")
            
        my_user = User.objects.create(username=uname,email=email)
        my_user.set_password(pass1)
        my_user.save()
        return redirect('login')

    return render (request,'users/register.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('website-home')
        else:
            messages.info("Username or Password is incorrect!!!")
    
    return render (request,'users/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')