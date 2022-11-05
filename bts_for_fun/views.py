from django.shortcuts import render

from .models import Station
# Create your views here.

def index(request):
    stations = Station.objects.all()
    return render(request, 'bts_for_fun/index.html',{
                   'stations' : stations,
        
    })
        
def stationdetail(request,station_id):
    station = Station.objects.get(id=station_id)
    return render(request, 'bts_for_fun/stationdetail.html',{
                   'station' : station,

    })