from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User
# Create your models here.

class Station(models.Model):
    thai_name_station = models.CharField(max_length=64)
    eng_name_station = models.CharField(max_length=64)
    code_station = models.CharField(max_length=64)
    station_detail_plan = models.TextField(blank = True)
    station_detail_exit = models.TextField(blank = True)
    station_pic = models.URLField(max_length=300, blank = True)
    
    def __str__(self):
        return f" {self.code_station} - {self.thai_name_station} ({self.eng_name_station})"
    

class Tourist(models.Model):
    thai_name_tourist = models.CharField(max_length=200)
    eng_name_tourist = models.CharField(max_length=200)
    on_station = models.ForeignKey(
        Station, on_delete=models.CASCADE, related_name="on_id_station")
    tourist_detail = models.TextField()
    #rating = models.SmallIntegerField(default=0)
    tourist_pic = models.URLField(max_length=300, blank = True)
    
    def average_rating(self) -> float:
        return Rating.objects.filter(tourist=self).aggregate(Avg("rating"))["rating__avg"] or 0
    def __str__(self):
        return f"{self.thai_name_tourist} ({self.eng_name_tourist}) {self.average_rating()}"

    
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.tourist.eng_name_tourist}: {self.rating}"