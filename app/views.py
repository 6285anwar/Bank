from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django. contrib import messages
# Create your views here.

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username  = request.POST['username']
        password = request.POST['password']

        if user_registration.objects.filter(username=username,password=password).exists():
            member=user_registration.objects.get(username = request.POST['username'],password = request.POST['password'])
            request.session['user_id'] = member.id
            request.session['usernamets1'] = member.username
            return redirect('user_home')
        else:
            messages.success(request, " Invalid credentials !! ")
            return redirect('login')

    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def user_register(request):
    if request.method == 'POST':
        user=user_registration()
        user.username = request.POST["username"]
        user.password = request.POST["password"]
        user.save()
        return redirect(login)

def user_home(request):
    if 'user_id' in request.session:
        if request.session.has_key('user_id'):
            user_id = request.session['user_id']
        else:
            return redirect('/')

        user = user_registration.objects.filter(id=user_id)
    return render(request, 'user_home.html',{'user':user})

def user_form(request):
    if 'user_id' in request.session:
        if request.session.has_key('user_id'):
            user_id = request.session['user_id']
        else:
            return redirect('/')

        user = user_registration.objects.filter(id=user_id)
    return render(request, 'user_form.html',{'user':user})

def form_save(request):
    if request.method == 'POST':
        form = data_form()
        form.name  = request.POST['name']
        form.dateofbirth  = request.POST['dob']
        form.age  = request.POST['age']
        form.gender  = request.POST['gender']
        form.mobile  = request.POST['phone']
        form.email  = request.POST['email']
        form.address  = request.POST['address']
        form.District  = request.POST['subject']
        form.Branch  = request.POST['topic']
        form.account  = request.POST['ac']
        form.meterials = request.POST.getlist('mp')
        form.save()
        
        messages.success(request, " Successfull !! ")
        return redirect('user_form')


def user_logout(request):
    if 'usernamets1' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')
