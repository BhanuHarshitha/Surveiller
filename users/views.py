from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm
# Create your views here.

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
            return redirect('index')
        else:
            messages.info("Username or Password is incorrect!!!")
    
    return render (request,'users/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('website-home')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        
        if u_form.is_valid():
            u_form.save()
       
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        
    context={
        'u_form':u_form,
    
    }
    return render(request, 'users/profile.html',context)