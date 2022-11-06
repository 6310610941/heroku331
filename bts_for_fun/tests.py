from django.test import TestCase, Client
from .models import Station
from django.urls import reverse
from django.db.models import Max


# Create your tests here.

class StationTestCase(TestCase):

    def setUp(self):
        station1 = Station.objects.create(thai_name_station='สถานี', eng_name_station='Sathanee', code_station='N00'  )
        station1 = Station.objects.create(thai_name_station='สถานีหนึ่ง', eng_name_station='first Sathanee', code_station='N01' )


    def test_index_codestatus(self):
        """ index page should return status code 200 """

        c = Client()
        response = c.get(reverse('bts_for_fun:index'))
        self.assertEqual(response.status_code, 200)



    def test_valid_stationdetail_page(self):
        """ valid station page should return status code 200 """

        c = Client()
        f = Station.objects.first()
        response = c.get(reverse('bts_for_fun:stationdetail', args=(f.id,)))
        self.assertEqual(response.status_code, 200)




    
