from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from login.models import Destination
# Create your views here.
def login(request):
    if request.method=='POST':
            
             uname=request.POST.get('uname')
             pword1=request.POST.get('pword1')
             user=auth.authenticate(username=uname,password=pword1)
             if user is not None:
                 auth.login(request,user)
                 post=Destination.objects.filter(username=uname)
                 print(post)
                 return render(request,'profile.html',{'dest':post})
             else:
                messages.info(request,'invalid')
                return render(request,'index.html')
    else:
        return render(request,'index.html')

def register(request):
    if request.method=='POST':
        first_name=request.POST.get('fname')
        last_name=request.POST.get('lname')
        username=request.POST.get('uname')
        password=request.POST.get('pword1')
        address=request.POST.get('address')
        email=request.POST.get('email')
        user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
        # user=Destination(first_name=first_name,last_name=last_name,username=username,password=password,email=email,address=address)
        if User.objects.filter(username=username).exists():
           messages.info(request,'uname taken')
           return redirect('/')
         
        else:
         user.save()
         print('user created')
        
        return redirect('/')
    else:
      return render(request,'register.html')