from django.urls import path

from . import views

app_name = 'bts_for_fun'

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:station_id>',views.stationdetail,name='stationdetail'),
]
