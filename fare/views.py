from django.shortcuts import render
from bts_for_fun.models import Station
import math

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'users/login.html')
    else:
        stations = Station.objects.all().order_by('pk')
        return render(request, 'fare/index.html',{
                   'stations' : stations,
    })
        

def result(request):
    if not request.user.is_authenticated:
        return render(request, 'users/login.html')
    else:
        entry = request.POST['entry']
        destination = request.POST['destination']
        name_entry = Station.objects.get(id=entry)
        name_destination = Station.objects.get(id=destination)
        data = abs(int(destination) - int(entry))

        
        if (int(entry) in range(1, 18)) and (int(destination) not in range(1,18)):
            data = abs(int(destination) - 17)

        elif (int(destination) in range(1, 18)) and (int(entry) not in range(1,18)):
            data = abs(17 - int(entry))
        
        if (int(entry) in range(1, 18)) and (int(destination) in range(1, 18)):
            result = 0
            
        elif (int(entry) in range(34, 49) and (int(destination) in range(34, 49))):
            result = 15

        elif data == 1:
            result = 16

        elif data == 2:
            result = 23

        elif data == 3:
            result = 26
        
        elif data == 4:
            result = 30
        
        elif data == 5:
            result = 33

        elif data == 6:
            result = 37

        elif data == 7:
            result = 40

        elif 8 <= data < 10:
            result = 44
        
        elif data >= 10:
            result = 59

        return render(request, 'fare/result.html',{
                   'result' : result,
                   'entry' : name_entry,
                   'destination' : name_destination,
        })
