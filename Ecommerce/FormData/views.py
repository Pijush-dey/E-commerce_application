
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from FormData.models import CustomerInfo

# Create your views here.

def SignUpPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            messages.error(request,'Username already exist')
        elif User.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR, 'Email already exist')
        else:
            user= CustomerInfo(username=username,email=email,password=password)
            user.save()
            messages.add_message(request, messages.SUCCESS, 'Your account is successfully created !')
            return redirect('SignIn')
    
    return render(request,"Sign_Up.html")


def SignInPage(request):
    message = messages.get_messages(request)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homePage')
        else:
            messages.add_message(request, messages.ERROR, 'Username or password is incorrect')
    return render(request,"Sign_In.html",{'message':message})