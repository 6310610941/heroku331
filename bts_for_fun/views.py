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
        tourists = Tourist.objects.filter(on_station=station)
        return render(request, 'bts_for_fun/stationdetail.html',{
                   'station' : station,
                   'tourists' : tourists,

    })


<<<<<<< HEAD
def touristdetail(request,station_id,tourist_id):
    if not request.user.is_authenticated:
        return render(request, 'users/login.html')
    else:
        station = Station.objects.get(id=station_id)
        tourists = Tourist.objects.filter(on_station=station)
        ta = Tourist.objects.get(id=tourist_id)
        return render(request, 'bts_for_fun/touristdetail.html',{
                   'station' : station,
                   'tourists' : tourists,
                   'ta' : ta,
    })
=======
#def touristdetail(request,tourist_id):
#    if not request.user.is_authenticated:
#        return render(request, 'users/login.html')
#    else:
#        tourist = Tourist.objects.get(id=tourist_id)

#        return render(request, 'bts_for_fun/touristdetail.html',{
#                   'tourist' : tourist,

#    })
>>>>>>> 1fa60e2093d5fc894dddcfb340d5f2a01c5ac2c2
