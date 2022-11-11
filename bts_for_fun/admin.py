from django.contrib import admin

from .models import Station, Stationdetail,Tourist,Touristdetail
# Register your models here.

admin.site.register(Station)
admin.site.register(Stationdetail)
admin.site.register(Tourist)
admin.site.register(Touristdetail)