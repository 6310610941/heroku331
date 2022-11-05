from django.test import TestCase, Client
from doctest import REPORT_CDIFF
from django.urls import reverse
from about import views
from urllib import request, response
from django.contrib.auth.models import User

#test signup_view

class SignUpPageTests(TestCase):
    def setUp(self) -> None:
        self.username = 'testuser'
        self.email = 'testuser@email.com'
        self.password = 'password123'

    def test_signup_page_url(self):
        """ sign up page view's status code is ok """

        c = Client()
        response = c.get(reverse('users:signup'))
        self.assertEqual(response.status_code, 200)


    def test_signup_form(self):
        """ can create user """

        response = self.client.post(reverse('users:signup'), data={
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': self.password
        })
        self.assertEqual(response.status_code, 200)

        users = User.objects.create_user(username= self.username,
            email= self.email,
            password= self.password)
        data = User.objects.all()
        self.assertEqual(data.count(), 1)

    def test_csnnot_signup_form(self):
        """ cannot create user """

        response = self.client.post(reverse('users:signup'), data={
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': 'password321'
        })
        self.assertEqual(response.status_code, 200)
