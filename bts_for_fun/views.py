from django.shortcuts import render

from .models import Station
# Create your views here.

def index(request):
    stations = Station.objects.all()
    return render(request, 'bts_for_fun/index.html',{
                   'stations' : stations
        
    })
        
    