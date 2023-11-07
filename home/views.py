from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .form import *

# Create your views here.


def home(request):
    post=Post.objects.all().order_by('-id')
    return render(request,'home.html',{'post':post})

def login_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
 
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request,'login.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'username is already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'email is already exists')

                return redirect('register')
                
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()
            return redirect('login')
    return render(request,'register.html')



def PostCreate(request):
    form=PostForm()
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form=PostForm()
            return redirect('home')
    return render(request,'createpost.html',{'form':form})


def Postupdate(request,id):
    obj=Post.objects.get(id=id)
    form=PostForm(request.POST or None,instance=obj)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            form=PostForm()
    return render(request,'updatepost.html',{'form':form})