from django.test import TestCase, Client
from django.urls import reverse


# Create your tests here.

class StationTestCase(TestCase):


    def test_index_codestatus(self):
        """ index page should return status code 200 """

        c = Client()
        response = c.get(reverse('about:index'))
        self.assertEqual(response.status_code, 200)

    def test_valid_about_us_page(self):
        """ valid about us page should return status code 200 """

        c = Client()
        response = c.get(reverse('about:about_us'))
        self.assertEqual(response.status_code, 200)
