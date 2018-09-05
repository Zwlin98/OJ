from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', context={'form': form})

def vlogin(request):
    if(request.method=='POST'):
        username = request.POST['username']
        password = request.POST['password']
        user =  authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('users:profile')
        else:
            return redirect('admin')
    else:
        return render(request,'users/login.html')

def success(requset):
    return HttpResponse("login success")

def vlogout(request):
    logout(request)
    return redirect('users:login')

def profile(request):
    if request.user.is_authenticated:
        return render(request,'users/profile.html',{'user': request.user })
    else:
        return redirect('users:login')