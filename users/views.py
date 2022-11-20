
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import SignUpForm, UpdateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

import users

# Create your views here.
log_in = 'users/login.html'

#def index(request):
#     if not request.user.is_authenticated:
#         return HttpResponseRedirect(reverse('users:login'))
#     return HttpResponseRedirect(reverse('about:index'))
#    pass

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('about:index'))
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
            return render(request, log_in)

    else:
        form = SignUpForm()

    return render(request, 'users/signup.html', {'form':form}, status=200)

@login_required(login_url='/users/login')
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()

            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='/users/profile')
    else:
        user_form = UpdateUserForm(instance=request.user)

    return render(request, 'users/profile.html', {'user_form': user_form })


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = '/users/login'