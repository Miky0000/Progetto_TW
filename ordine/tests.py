import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, resolve
from .models import Ordine
from .views import OrdineListView, RimborsiListView, Checkout, Contatto, RecensioneView, Restituisci
from .forms import CheckoutForm


class TestUrls(TestCase):

    def test_ordine_list_url_resolve(self):
        url = reverse('ordine:ordine-list')
        self.assertEqual(resolve(url).func.view_class, OrdineListView)

    def te_rimborsi_list_url_resolve(self):
        url = reverse('ordine:rimborsi-list')
        self.assertEqual(resolve(url).func.view_class, RimborsiListView)

    def test_checkout_url_resolve(self):
        url = reverse('ordine:checkout')
        self.assertEqual(resolve(url).func, Checkout)

    def test_contatto_url_resolve(self):
        url = reverse('ordine:contatto-page')
        self.assertEqual(resolve(url).func, Contatto)

    def test_recensione_url_resolve(self):
        url = reverse('ordine:recensione-page')
        self.assertEqual(resolve(url).func, RecensioneView)

    def test_restituisci_url_resolve(self):
        url = reverse('ordine:restituisci-page', args=[1])
        self.assertEqual(resolve(url).func, Restituisci)


class TestViews(TestCase):

    def test_ordine_list_response(self):
        response = self.client.get(reverse('ordine:ordine-list'))
        self.assertEqual(response.status_code, 302)

    def test_rimborsi_list_response(self):
        response = self.client.get(reverse('ordine:rimborsi-list'))
        self.assertEqual(response.status_code, 302)

    def tes_checkout_response(self):
        response = self.client.get(reverse('ordine:checkout'))
        self.assertEqual(response.status_code, 302)

    def test_contatto_response(self):
        response = self.client.get(reverse('ordine:contatto-page'))
        self.assertEqual(response.status_code, 302)

    def test_recensione_response(self):
        response = self.client.get(reverse('ordine:recensione-page'))
        self.assertEqual(response.status_code, 302)

    def test_restituisci_response(self):
        response = self.client.get(reverse('ordine:restituisci-page', args=[1]))
        self.assertEqual(response.status_code, 302)


class TestModels(TestCase):

    def setUp(self):
        self.ordine = Ordine.objects.create(
            image='e',
            prodotto='e',
            prod_id=1,
            user=User.objects.create(),
            prezzo=1,
            quantity=1,
            totale=1,
            indirizzo='i',
            email='i',
            telefono=1,
            data=datetime.datetime.now(),
        )

    def test_ordine_default_check(self):
        self.assertFalse(self.ordine.spedito, 'spedito errato')
        self.assertFalse(self.ordine.restituito, 'restituito errato')


class TestForms(TestCase):

    def test_form_is_valid(self):
        form = CheckoutForm(data={
            'telefono': 1234567890,
            'indirizzo': 'es',
            'email': 'e@example.com',
            'carta': 1000000000000000,
            'scadenza': datetime.datetime.now(),
            'cvv': 222,
        })

        self.assertEqual(len(form.errors), 1)

    def test_form_no_data(self):
        form = CheckoutForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 6)
