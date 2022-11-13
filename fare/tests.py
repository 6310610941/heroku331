from django.test import TestCase, Client
from doctest import REPORT_CDIFF
from django.urls import reverse
from users import views
from urllib import request, response
from django.contrib.auth.models import User
from bts_for_fun.models import Station

# Create your tests here.

class FarePageTests(TestCase):
    def setUp(self):
            #create user
            self.user = User.objects.create_user('test_user', password='test_pass')
            station1 = Station.objects.create(thai_name_station='คูคต', eng_name_station='Khu Khot', code_station='N24', station_detail='-', id=1)
            station2 = Station.objects.create(thai_name_station='แยก คปอ.', eng_name_station='Yaek Kor Por Aor', code_station='N23', station_detail='-', id=2)
            station3 = Station.objects.create(thai_name_station='สยาม', eng_name_station='Siam Station', code_station='CEN', station_detail='-', id=25)
            station4 = Station.objects.create(thai_name_station='ราชเทวี', eng_name_station='Ratchathewi', code_station='N1', station_detail='-', id = 24)
            station5 = Station.objects.create(thai_name_station='พญาไท', eng_name_station='Phaya Thai', code_station='N2', station_detail='-', id=23)
            station6 = Station.objects.create(thai_name_station='อนุสาวรีย์ชัยสมรภูมิ', eng_name_station='Victory Monument', code_station='N3', station_detail='-', id=22)
            station7 = Station.objects.create(thai_name_station='สนามเป้า', eng_name_station='Sanam Pao', code_station='N4', station_detail='-', id=21)
            station8 = Station.objects.create(thai_name_station='อารีย์', eng_name_station='Ari', code_station='N5', station_detail='-', id=20)
            station9 = Station.objects.create(thai_name_station='เสนาร่วม', eng_name_station='Sena Rua', code_station='N6', station_detail='-', id=19)
            station10 = Station.objects.create(thai_name_station='สะพานควาย', eng_name_station='Saphan Khwai', code_station='N7', station_detail='-', id=18)
            station11 = Station.objects.create(thai_name_station='หมอชิต', eng_name_station='Mo Chit', code_station='N8', station_detail='-', id=17)
            station12 = Station.objects.create(thai_name_station='อ่อนนุช', eng_name_station='On Nut', code_station='E9', station_detail='-', id=34)
            station13 = Station.objects.create(thai_name_station='บางจาก', eng_name_station='Bang Chak', code_station='E10', station_detail='-', id=35)

    def test_login_view_status_code_from_fare_page(self):
        """ login view's status code is ok """

        c = Client()
        response = c.get(reverse('fare:index'))
        self.assertEqual(response.status_code, 200)

    def test_login_view_status_code_from_result_page(self):
        """ login view's status code is ok """

        c = Client()
        response = c.get(reverse('fare:result'))
        self.assertEqual(response.status_code, 200)

    def test_fare_view_status_code(self):
        """ fare view's status code is ok """

        c = Client()
        c.login(username='test_user', password='test_pass')
        response = c.get(reverse('fare:index'))
        self.assertEqual(response.status_code, 200)

    def test_result_view_status_code(self):
        """ result view's status code is ok """

        c = Client()
        c.login(username='test_user', password='test_pass')
        entry = 1
        destination = 2
        response = c.post(reverse('fare:result'), {'entry' : entry, 'destination' : destination,})
        self.assertEqual(response.status_code, 200)

    def test_result_view_condition_1(self):
        """ test result condition 1 """

        c = Client()
        c.login(username='test_user', password='test_pass')
        entry = 34
        destination = 35
        response = c.post(reverse('fare:result'), {'entry' : entry, 'destination' : destination,})
        self.assertEqual(response.status_code, 200)

    def test_result_view_condition_2(self):
        """ test result condition 2 """


        c = Client()
        c.login(username='test_user', password='test_pass')
        entry = 25
        destination = 24
        response = c.post(reverse('fare:result'), {'entry' : entry, 'destination' : destination,})
        self.assertEqual(response.status_code, 200)

    def test_result_view_condition_3(self):
        """ test result condition 3 """

        c = Client()
        c.login(username='test_user', password='test_pass')
        entry = 25
        destination = 23
        response = c.post(reverse('fare:result'), {'entry' : entry, 'destination' : destination,})
        self.assertEqual(response.status_code, 200)

    def test_result_view_condition_4(self):
        """ test result condition 4 """

        c = Client()
        c.login(username='test_user', password='test_pass')
        entry = 17
        destination = 20
        response = c.post(reverse('fare:result'), {'entry' : entry, 'destination' : destination,})
        self.assertEqual(response.status_code, 200)

    def test_result_view_condition_5(self):
        """ test result condition 5 """
        
        c = Client()
        c.login(username='test_user', password='test_pass')
        entry = 25
        destination = 21
        response = c.post(reverse('fare:result'), {'entry' : entry, 'destination' : destination,})
        self.assertEqual(response.status_code, 200)

    def test_result_view_condition_6(self):
        """ test result condition 6 """

        c = Client()
        c.login(username='test_user', password='test_pass')
        entry = 25
        destination = 20
        response = c.post(reverse('fare:result'), {'entry' : entry, 'destination' : destination,})
        self.assertEqual(response.status_code, 200)

    def test_result_view_condition_7(self):
        """ test result condition 7 """

        c = Client()
        c.login(username='test_user', password='test_pass')
        entry = 25
        destination = 19
        response = c.post(reverse('fare:result'), {'entry' : entry, 'destination' : destination,})
        self.assertEqual(response.status_code, 200)

    def test_result_view_condition_8(self):
        """ test result condition 8 """

        c = Client()
        c.login(username='test_user', password='test_pass')
        entry = 25
        destination = 18
        response = c.post(reverse('fare:result'), {'entry' : entry, 'destination' : destination,})
        self.assertEqual(response.status_code, 200)

    def test_result_view_condition_9(self):
        """ test result condition 9 """

        c = Client()
        c.login(username='test_user', password='test_pass')
        entry = 25
        destination = 17
        response = c.post(reverse('fare:result'), {'entry' : entry, 'destination' : destination,})
        self.assertEqual(response.status_code, 200)

    def test_result_view_condition_10(self):
        """ test result condition 10 """

        c = Client()
        c.login(username='test_user', password='test_pass')
        entry = 1
        destination = 34
        response = c.post(reverse('fare:result'), {'entry' : entry, 'destination' : destination,})
        self.assertEqual(response.status_code, 200)

    def test_result_view_condition_11(self):
        """ test result condition 11 """

        c = Client()
        c.login(username='test_user', password='test_pass')
        entry = 17
        destination = 20
        response = c.post(reverse('fare:result'), {'entry' : entry, 'destination' : destination,})
        self.assertEqual(response.status_code, 200)