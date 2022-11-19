from django.contrib import admin

from .models import Station,Tourist,Rating
# Register your models here.

admin.site.register(Station)
admin.site.register(Tourist)
admin.site.register(Rating)