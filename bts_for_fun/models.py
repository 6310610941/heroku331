from django.db import models

# Create your models here.

class Station(models.Model):
    thai_name_station = models.CharField(max_length=64)
    eng_name_station = models.CharField(max_length=64)
    code_station = models.CharField(max_length=64)
    station_detail = models.TextField()
    
    def __str__(self):
        return f" {self.code_station} - {self.thai_name_station} ({self.eng_name_station})"
    
