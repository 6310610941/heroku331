from django.test import TestCase, Client
from doctest import REPORT_CDIFF
from django.urls import reverse
from about import views
from urllib import request, response
from django.contrib.auth.models import User

#test signup_view

class SignUpPageTests(TestCase):

    def test_signup_page_url(self):
        """ sign up page view's status code is ok """
        c = Client()
        response = c.post(reverse('users:signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_form(self):
        """ can create user """

        response = self.client.post(reverse('users:signup'), {'username': 'harry', 'name': 'draco', 'surname': 'malfoy','email': 'draco@cn331.com', 'password1': 'darry123', 'password2': 'darry123'})
        self.assertEqual(response.status_code, 200)

    def test_cannot_signup_form(self):
        """ cannot create user """

        response = self.client.post(reverse('users:signup'), {'username': 'harry', 'name': 'draco', 'surname': 'malfoy','email': 'draco@cn331.com', 'password1': 'darry123', 'password2': 'harry123'})
        self.assertEqual(response.status_code, 200)


class LoginPageTests(TestCase):
    def setUp(self):
        #create user
        self.user = User.objects.create_user('test_user', password='test_pass')
        #c = Client()
        #c.login(username='test_user', password='test_pass')

    def test_login_view_status_code(self):
        """ login view's status code is ok """

        c = Client()
        response = c.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)

    def test_login_success(self):
        """ login success """
        c = Client()
        c.login(username='test_user', password='test_pass')
        response = c.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)

    def test_login_fail(self):
        """ wrong username or password """
        c = Client()
        c.login(username='wrong_user', password='wrong_pass')
        response = c.get(reverse('users:index'))
        self.assertEqual(response.status_code, 302)

