from django.contrib.auth.models import User
from django.db.models import Max
from django.test import Client, TestCase
from django.urls import reverse
from .models import Station, Tourist, Rating

# Create your tests here.

class StationTestCase(TestCase):
    
    
    def setUp(self):
        user = User.objects.create_superuser(username='test_user', password='test_pass')
        station1 = Station.objects.create(thai_name_station='สถานี', eng_name_station='Sathanee', code_station='N00' , id=1  )
        station2 = Station.objects.create(thai_name_station='สถานีหนึ่ง', eng_name_station='first Sathanee', code_station='N01', )
        tour1 = Tourist.objects.create(thai_name_tourist='ตลาด', eng_name_tourist='market', on_station=station1 )
        tour2 = Tourist.objects.create(thai_name_tourist='สวน', eng_name_tourist='park', on_station=station2)
        rating1 = Rating.objects.create(user=user, tourist=tour1, rating=4)

    def test_invalid_authen_index(self):
        """ should return http unauthorize status """
        c = Client()
        logged_in = c.login(username='test_user', password='123456789')
        self.assertFalse(logged_in)

        response = c.get(reverse('bts_for_fun:index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')


    def test_valid_authen_index(self):
        """ login's user can view station """
        c = Client()
        logged_in = c.login(username='test_user', password='test_pass')
        self.assertTrue(logged_in)
        response = c.get(reverse('bts_for_fun:index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bts_for_fun/index.html')


    def test_invalid_authen_stationdetail_page(self):
        """ should return http unauthorize status """
        c = Client()
        logged_in = c.login(username='test_user', password='123456789')

        f = Station.objects.first()
        response = c.post(reverse('bts_for_fun:stationdetail', args=(f.id,)))
        self.assertTemplateUsed(response, 'users/login.html')

    def test_valid_stationdetail_page(self):
        """ login's user can view station detail """
        c = Client()
        c.login(username='test_user', password='test_pass')
        f = Station.objects.first()
        response = c.post(reverse('bts_for_fun:stationdetail', args=(f.id,)))
        self.assertEqual(response.status_code, 200)



    def test_valid_tourist_view(self):
        """ login's user can view tourist attraction name """
        c = Client()
        c.login(username='test_user', password='test_pass')
        q = Tourist.objects.first()

        response = c.post(reverse('bts_for_fun:stationdetail', args=(q.id,)))
        self.assertEqual(response.status_code, 200)


    
    def test_valid_touristdetail_page(self):
        """ login's user can view tourist attraction detail """
        c = Client()
        c.login(username='test_user', password='test_pass')
        q = Tourist.objects.first()

        response = c.post(reverse('bts_for_fun:touristdetail', args=(q.id,)))
        self.assertEqual(response.status_code, 200)
        
    def test_object_name_is_thai_name_tourist_eng_name_tourist(self):
        """ check object in tourist attraction detail(detail) """
        t = Tourist.objects.get(id=1)
        expected_object_name = f'{t.thai_name_tourist} ({t.eng_name_tourist}) {t.average_rating()}'
        self.assertEqual(str(t), expected_object_name)

    def test_object_name_is_tourist_eng_name_rating(self):
        """ check object in tourist attraction detail(rating) """
        r = Rating.objects.get(id=1)
        expected_object_name = f'{r.tourist.eng_name_tourist}: {r.rating}'
        self.assertEqual(str(r), expected_object_name)

    def test_rating(self):
        """ can vote for rating """
        c = Client()
        c.login(username='test_user', password='test_pass')
        q = Tourist.objects.first()
        r = Rating.objects.first()

        response = c.post(reverse('bts_for_fun:rating', args=(q.id,r.id)))
        self.assertEqual(response.status_code, 200)