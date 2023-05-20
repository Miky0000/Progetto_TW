from django.test import TestCase
from django.urls import reverse, resolve
from .views import cart_add, item_clear, item_decrement, item_increment, cart_clear, cart_detail


class TestUrls(TestCase):

    def test_cart_add_url_resolve(self):
        url = reverse('carrello:cart_add', args=[1])
        self.assertEqual(resolve(url).func, cart_add)

    def test_item_clear_url_resolve(self):
        url = reverse('carrello:item_clear', args=[1])
        self.assertEqual(resolve(url).func, item_clear)

    def test_item_decrement_url_resolve(self):
        url = reverse('carrello:item_decrement', args=[1])
        self.assertEqual(resolve(url).func, item_decrement)

    def test_item_increment_url_resolve(self):
        url = reverse('carrello:item_increment', args=[1])
        self.assertEqual(resolve(url).func, item_increment)

    def test_cart_clear_url_resolve(self):
        url = reverse('carrello:cart_clear')
        self.assertEqual(resolve(url).func, cart_clear)

    def test_cart_detail_url_resolve(self):
        url = reverse('carrello:cart_detail')
        self.assertEqual(resolve(url).func, cart_detail)


class TestViews(TestCase):

    def test_cart_add_response(self):
        response = self.client.get(reverse('carrello:cart_add', args=[1]))
        self.assertEqual(response.status_code, 302)

    def test_item_clear_response(self):
        response = self.client.get(reverse('carrello:item_clear', args=[1]))
        self.assertEqual(response.status_code, 302)

    def test_item_de_response(self):
        response = self.client.get(reverse('carrello:item_decrement', args=[1]))
        self.assertEqual(response.status_code, 302)

    def test_item_in_response(self):
        response = self.client.get(reverse('carrello:item_increment', args=[1]))
        self.assertEqual(response.status_code, 302)

    def test_cart_clear_response(self):
        response = self.client.get(reverse('carrello:cart_clear'))
        self.assertEqual(response.status_code, 302)

    def test_cart_detail_response(self):
        response = self.client.get(reverse('carrello:cart_detail'))
        self.assertEqual(response.status_code, 302)
