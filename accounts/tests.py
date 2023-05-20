import datetime
from django.test import TestCase
from django.urls import reverse, resolve
from .views import ProfileView, UserDeleteView, Modifica, Register
from .forms import RegistrationForm


class TestUrls(TestCase):

    def test_profile_url_resolve(self):
        url = reverse('accounts:profile')
        self.assertEqual(resolve(url).func.view_class, ProfileView)

    def test_user_delete_view_url_resolve(self):
        url = reverse('accounts:delete_profile', args=[1])
        self.assertEqual(resolve(url).func.view_class, UserDeleteView)

    def test_modifica_url_resolve(self):
        url = reverse('accounts:modifica')
        self.assertEqual(resolve(url).func, Modifica)

    def test_register_url_resolve(self):
        url = reverse('accounts:register')
        self.assertEqual(resolve(url).func, Register)


class TestViews(TestCase):

    def test_profile_response(self):
        response = self.client.get(reverse('accounts:profile'))
        self.assertEqual(response.status_code, 302)

    def test_user_delete_view_response(self):
        response = self.client.get(reverse('accounts:delete_profile', args=[1]))
        self.assertEqual(response.status_code, 302)

    def test_modifica_response(self):
        response = self.client.get(reverse('accounts:modifica'))
        self.assertEqual(response.status_code, 302)

    def test_register_response(self):
        response = self.client.get(reverse('accounts:profile'))
        self.assertEqual(response.status_code, 302)


class TestForms(TestCase):

    def setUp(self):
        self.form = RegistrationForm(data={
            'username': 'p',
            'first_name': 'p',
            'last_name': 'p',
            'birthday': datetime.datetime.now(),
            'email': 'p@example.com',
        })

    def test_Registration_forms_is_valid(self):
        self.assertEqual(len(self.form.errors), 3)

    def test_registration_form_no_data(self):
        form = RegistrationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)
