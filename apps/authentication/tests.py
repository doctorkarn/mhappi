from django.test import TestCase
from django.contrib.auth.models import User
from apps.authentication.models import Patient, Officer
from django.core.urlresolvers import reverse
from django.contrib.auth.hashers import make_password


# Create your tests here.
class LoginViewTests(TestCase):
    def test_login_view_with_no_input(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "MHAPPI")

    def test_login_view_with_invalid_input(self):
        response = self.client.post(reverse('login'), {'username':'username', 'password':'password'}, follow=True, secure=False)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Username or Password is invalid")

    def test_login_view_with_valid_input(self):
        user = User.objects.create_user('patient01', 'patient01@example.com', 'patient01') 
        logged_in = self.client.login(username="patient01", password="patient01")
        self.assertTrue(logged_in) 
        session = self.client.session
        session['user_role'] = 'patient'
        session.save()
        response = self.client.get(reverse('home'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "patient01")
        self.assertContains(response, "Logout")
        self.client.logout()
        # session['user_role'] = ''
        # session.save()
        response = self.client.get(reverse('home'), follow=True)
        self.assertContains(response, "Please Login")
