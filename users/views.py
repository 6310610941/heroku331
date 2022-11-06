
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import SignUpForm

import users

# Create your views here.
log_in = 'users/login.html'

def index(request):
#     if not request.user.is_authenticated:
#         return HttpResponseRedirect(reverse('users:login'))
#     return HttpResponseRedirect(reverse('about:index'))
    pass

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('users:index'))
        else:
            return render(request, log_in, {
                'message': 'Invalid credentials.'
            })
    return render(request, log_in)

def logout_view(request):
    logout(request)
    return render(request, log_in, {
                'message': 'You are logged out.'
            })

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'users/login.html')
    else:
        form = SignUpForm()
        return render(request, 'users/signup.html', {'form':form}, status=200)