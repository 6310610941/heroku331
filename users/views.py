
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

import users

# Create your views here.


def index(request):
    return render(request, "users/index.html", {
    })
