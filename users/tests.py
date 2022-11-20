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
        response = c.get(reverse('users:signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_form(self):
        """ can create user """

        response = self.client.post(reverse('users:signup'), {'username': 'harry', 'name': 'draco', 'surname': 'malfoy','email': 'draco@cn331.com', 'password1': 'darry123', 'password2': 'darry123'})
        self.assertEqual(response.status_code, 200)

    def test_cannot_signup_form(self):
        """ cannot create user """

        response = self.client.get(reverse('users:signup'), {'username': 'harry', 'name': 'draco', 'surname': 'malfoy','email': 'draco@cn331.com', 'password1': 'darry123', 'password2': 'harry123'})
        self.assertEqual(response.status_code, 200)


class LoginPageTests(TestCase):
    def setUp(self):
        #create user
        self.user = User.objects.create_user('test_user', password='test_pass')

    def test_login_view_status_code(self):
        """ login view's status code is ok """

        c = Client()
        response = c.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)

    def test_login_success(self):
        """ login success """
        self.assertTrue(isinstance(self.user, User))
        login = self.client.login(username='test_user', password='test_pass')
        self.assertEqual(login, True)

    def test_login_fail(self):
        """ wrong username or password """
        self.assertTrue(isinstance(self.user, User))
        login = self.client.login(username='wrong_user', password='wrong_pass')
        self.assertEqual(login, False)

    def test_login_view_success(self):
        """ login view success """
        c = Client()
        c.login(username='test_user', password='test_pass')
        response = c.post(reverse('users:login'), {"username": "test_user", "password": "test_pass"}, follow=True)
        self.assertEquals(response.status_code, 200)

    def test_login_view_failed(self):
        """ login view fail """
        c = Client()
        response = c.post(reverse('users:login'), {"username": "", "password": "12345"}, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        """ logout success """
        self.assertTrue(isinstance(self.user, User))
        self.client.logout()
        response = self.client.get(reverse('users:logout'))
        self.assertTemplateUsed(response, "users/login.html")
        
class ProfilePageTests(TestCase):
    def setUp(self):
        #create user
        self.user = User.objects.create_user('test_user', password='test_pass')
        

    def test_profile_view_status_code(self):
        """ profile view's status code is ok """
        
        c = Client()
        c.login(username='test_user', password='test_pass')
        response = c.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 200)

    def test_change_password_status_code(self):
        """ change_password's status code is ok """

        c = Client()
        c.login(username='test_user', password='test_pass')
        response = c.get(reverse('users:change_password'))
        self.assertEqual(response.status_code, 200)
    
    def test_profile_form_1(self):
        """ can edit username """
        c = Client()
        c.login(username='test_user', password='test_pass')
        c.post(reverse('users:signup'), {'username': 'test_user', 'first_name': 'test_name', 'last_name': 'test_surname','email': 'test@cn331.com', 'password1': 'test_pass', 'password2': 'test_pass'})
        c.post(reverse('users:profile'), {'username': 'edited_user', 'first_name': 'edited_name', 'last_name': 'edited_surname','email': 'edited@cn331.com'})
        response = c.get(reverse('users:profile'))
        self.assertContains(response, 'edited_user')


    def test_profile_form_2(self):
        """ can edit email """
        c = Client()
        c.login(username='test_user', password='test_pass')
        c.post(reverse('users:signup'), {'username': 'test_user', 'first_name': 'test_name', 'last_name': 'test_surname','email': 'test@cn331.com', 'password1': 'test_pass', 'password2': 'test_pass'})
        c.post(reverse('users:profile'), {'username': 'edited_user', 'first_name': 'edited_name', 'last_name': 'edited_surname','email': 'edited@cn331.com'})
        response = c.get(reverse('users:profile'))
        self.assertContains(response, 'edited@cn331.com')

    def test_profile_form_3(self):
        """ can edit name """
        c = Client()
        c.login(username='test_user', password='test_pass')
        c.post(reverse('users:signup'), {'username': 'test_user', 'first_name': 'test_name', 'last_name': 'test_surname','email': 'test@cn331.com', 'password1': 'test_pass', 'password2': 'test_pass'})
        c.post(reverse('users:profile'), {'username': 'edited_user', 'first_name': 'edited_name', 'last_name': 'edited_surname','email': 'edited@cn331.com'})
        response = c.get(reverse('users:profile'))
        self.assertContains(response, 'edited_name')


    def test_profile_form_4(self):
        """ can edit surname """
        c = Client()
        c.login(username='test_user', password='test_pass')
        c.post(reverse('users:signup'), {'username': 'test_user', 'first_name': 'test_name', 'last_name': 'test_surname','email': 'test@cn331.com', 'password1': 'test_pass', 'password2': 'test_pass'})
        c.post(reverse('users:profile'), {'username': 'edited_user', 'first_name': 'edited_name', 'last_name': 'edited_surname','email': 'edited@cn331.com'})
        response = c.get(reverse('users:profile'))
        self.assertContains(response, 'edited_surname')

class ChangePasswordPageTests(TestCase):
    def setUp(self):
        #create user
        self.user = User.objects.create_user('test_user', password='test_pass')

    def test_change_password(self):
        """ can change password """
        c = Client()
        c.login(username='test_user', password='test_pass')
        c.post(reverse('users:change_password'), {'old_password': 'test_pass', 'new_password1': 'new_pass', 'new_password2': 'new_pass'})
        c.logout()
        c.login(username='test_user', password='new_pass')
        response = c.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 200)

    def test_wrong_password(self):
        """ wrong password """
        c = Client()
        c.login(username='test_user', password='test_pass')
        c.post(reverse('users:change_password'), {'old_password': 'wrong_pass', 'new_password1': 'new_pass', 'new_password2': 'new_pass'})
        c.logout()
        c.login(username='test_user', password='new_pass')
        response = c.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 302)