from django.test import TestCase, Client
from doctest import REPORT_CDIFF
from django.urls import reverse
from about import views
from urllib import request, response
from django.contrib.auth.models import User, Request

# Create your tests here.

#test signup_view

class UserViewTestCase(TestCase):
    
    def setUp(self):
        # create user
        user = User.objects.create_user(username='draco', email='draco@cn331.com', password='dracopassword')

    def test_homepage_view_status_code(self):
        """ main page view's status code is ok """

        c = Client()
        response = c.get(reverse('about:index'))
        self.assertEqual(response.status_code, 200)

    def test_user_signup(self):
        """ correct username, email, password can sign up """
        c = Client()
        response = c.post(reverse('users:signup'),
                {'username': 'dracomalfoy', 'name': 'draco', 'surname': 'malfoy', 'email': 'draco@cn331.com', 'password1': 'malfoy123', 'password2': 'malfoy123' })
        self.assertEqual(response.status_code, 302)

        response = c.get(reverse('users:signup'))
        self.assertEqual(response.status_code, 200)

    def test_user_cannot_signup(self):
        """ wrong username, email, password can sign up """
        c = Client()
        response = c.post(reverse('users:signup'),
                {'username': 'dracomalfoy', 'name': 'draco', 'surname': 'malfoy', 'email': 'draco@cn331.com', 'password1': 'malfoy123', 'password2': 'malfoy321' })
        self.assertEqual(response.status_code, 200)

        response = c.get(reverse('users:login'))
        self.assertEqual(response.status_code, 302)

    