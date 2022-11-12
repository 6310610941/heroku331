from django.db import models

# Create your models here.

class Station(models.Model):
    thai_name_station = models.CharField(max_length=64)
    eng_name_station = models.CharField(max_length=64)
    code_station = models.CharField(max_length=64)
    station_detail = models.TextField()
    stt_pic = models.ImageField(upload_to='static/stationpic/', blank = True)
    
    def __str__(self):
        return f" {self.code_station} - {self.thai_name_station} ({self.eng_name_station})"
    

class Tourist(models.Model):
    thai_name_tourist = models.CharField(max_length=200)
    eng_name_tourist = models.CharField(max_length=200)
    on_station = models.ForeignKey(
        Station, on_delete=models.CASCADE, related_name="on_id_station")
    tourist_detail = models.TextField()
    comment = models.TextField()
    rating = models.SmallIntegerField(default=0)
    t_pic = models.ImageField(upload_to='static/touristpic/', blank = True)
    
    def __str__(self):
        return f"{self.thai_name_tourist} ({self.eng_name_tourist})"
    
