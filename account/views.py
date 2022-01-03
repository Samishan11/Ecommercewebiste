
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.http import HttpResponse , JsonResponse
from django.core.checks import messages
from .models import *
# Create your views here.

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            if User.objects.filter(username=name).exists():
                messages.Info(request,'Username is already taken')
                return redirect('/account/signup')
            elif User.objects.filter(email=email).exists():
                messages.Info(request,'email is already taken')
                return redirect('/account/signup')
            else:
                user = User.objects.create_user(username = name , email = email, password= password1)
                user.save()
                messages.Info(request,'Register succfully')
                if user: 
                    profile = Profile.objects.create(phone=phone ,user = user)
                    profile.save()
                return redirect('/account/signup')
        else:
            messages.Info(request,'password not match')
    return render(request, 'signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            if not user.is_staff:
                auth.login(request,user)
                return redirect('/')
            elif user.is_staff:
                auth.login(request,user)
                return redirect('/admin')
        else:
            messages.Info(request, 'Username or password not match')
    return render(request,'signin.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
        

