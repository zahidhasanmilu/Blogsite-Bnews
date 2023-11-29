from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User

from .models import User_Profile
from .forms import ProfilePicForm

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.success(request, 'User Already Exists')
                return redirect('register-url')
            elif User.objects.filter(email=email).exists():
                messages.success(request, 'Email Already Exists')
                return redirect('register-url')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.set_password(password)
                user.save()
                messages.success(request, 'Account created')
                return redirect('home')
        else:
            messages.success(request, 'password not match')
            return redirect('register-url')
    return render(request, 'App_Login/register.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successfully !')
            return redirect('home')
        else:
            messages.success(request, 'Input Invalid')
            return redirect('signin-url')
    return render(request, 'App_Login/login.html')


@login_required
def signout(request):
    logout(request)
    messages.success(request, 'Loogout Succesful')
    return redirect('signin-url')


@login_required
def profile(request):
    return render(request, 'App_Login/profile.html')

@login_required
def profileUpdate(request):
    current_user = request.user
    form = UserChangeForm(instance=current_user)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            # form = UserChangeForm(request.POST, instance=current_user)
            messages.success(request, 'Profile update Succesful')
            return redirect('profile-url')

    context = {
        'form': form
    }
    return render(request, 'App_Login/update_profile.html', context)

@login_required
def addProfile_pic(request):
    form = ProfilePicForm(request.FILES)
    if request.method == "POST":
        form = ProfilePicForm(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()  
            messages.success(request, 'Profile Pic Update Succesfully Done')
            return redirect('profile-url')
    context = {
        'form': form
    }
    return render(request, 'App_Login/update_profile_pic.html', context)

@login_required
def update_profile_pic(request):
    form = ProfilePicForm(request.FILES, instance=request.user.user_profile)
    if request.method == "POST":
        form = ProfilePicForm(request.POST, request.FILES,
                              instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Pic Update Succesfully Done')
            return redirect('profile-url')

    context = {
        'form': form
    }
    return render(request, 'App_Login/update_profile_pic.html', context)
