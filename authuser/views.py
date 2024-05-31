from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from authuser.models import User
from django.contrib.auth.hashers import make_password
from authuser.forms import LoginForm, UserRegistrationForm

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email =  form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.validate_login(email,password)
                login(request, user)
                user = user.get_full_name()
                return render(request,'login.html',{'login':True,'name':user})
            except ValueError as e:
                return render(request,'login.html',{'form':form,'login':False})
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form,'user':request.user})

def user_logout(request):
    logout(request)
    return redirect('login')


def register_user(request):
    print(request.method)
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            print(user.password)
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    return render(request,'home.html',{'form':form})