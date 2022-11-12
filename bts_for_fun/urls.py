from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'bts_for_fun'

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:station_id>',views.stationdetail,name='stationdetail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
