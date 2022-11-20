from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Station, Tourist, Rating

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'users/login.html')
    else:
        stations = Station.objects.all().order_by('pk')
        return render(request, 'bts_for_fun/index.html',{
                   'stations' : stations,
        
    })
        
def stationdetail(request,station_id):
    if not request.user.is_authenticated:
        return render(request, 'users/login.html')
    else:
        station = Station.objects.get(id=station_id)
        tourists = Tourist.objects.filter(on_station=station).order_by('-rating')
        return render(request, 'bts_for_fun/stationdetail.html',{
                   'station' : station,
                   'tourists' : tourists,

    })


def touristdetail(request,tourist_id):
    tourists = Tourist.objects.filter(id=tourist_id)
    for tour in tourists:
        rating = Rating.objects.filter(tourist=tour, user=request.user).first()
        tour.user_rating = rating.rating if rating else 0
    rating = Rating.objects.filter(tourist=tour, user=request.user).first()
    tourist = Tourist.objects.get(id=tourist_id)

    return render(request, 'bts_for_fun/touristdetail.html',{
                   'tourist' : tourist,  "tourists": tourists, 'rating' : rating

    })

def rate(request: HttpRequest, tourist_id: int, rating: int) -> HttpResponse:
    tourist = Tourist.objects.get(id=tourist_id)
    Rating.objects.filter(tourist=tourist, user=request.user).delete()
    tourist.rating_set.create(user=request.user, rating=rating)
    return index(request)

