from django.shortcuts import render

from .models import Station,Tourist
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'users/login.html')
    else:
        stations = Station.objects.all()
        return render(request, 'bts_for_fun/index.html',{
                   'stations' : stations,
        
    })
        
def stationdetail(request,station_id):
    if not request.user.is_authenticated:
        return render(request, 'users/login.html')
    else:
        station = Station.objects.get(id=station_id)

        return render(request, 'bts_for_fun/stationdetail.html',{
                   'station' : station,

    })