from django.test import TestCase
from django.urls import reverse, resolve
from .views import ProdottoListView, ProdottoDetailView, CercaView
from .models import Prodotto


class TestUrls(TestCase):

    def test_prodotto_list_url_resolve(self):
        url = reverse('prodotto:prodotto-list')
        self.assertEqual(resolve(url).func.view_class, ProdottoListView)

    def test_prodotto_list_tag_url_resolve(self):
        url = reverse('prodotto:prodotto-list', args=['AL'])
        self.assertEqual(resolve(url).func.view_class, ProdottoListView)

    def test_prodotto_detail_url_resolve(self):
        url = reverse('prodotto:prodotto-detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, ProdottoDetailView)

    def test_cerca_url_resolve(self):
        url = reverse('prodotto:cerca')
        self.assertEqual(resolve(url).func.view_class, CercaView)


class TestViews(TestCase):

    def test_cerca_response(self):
        response = self.client.get(reverse('prodotto:cerca'))
        self.assertEqual(response.status_code, 200)

    def test_prodotto_list_response(self):
        response = self.client.get(reverse('prodotto:prodotto-list'))
        self.assertEqual(response.status_code, 200)

    def test_prodotto_list_tag_response(self):
        response = self.client.get(reverse('prodotto:prodotto-list', args=['AL']))
        self.assertEqual(response.status_code, 200)

    # def test_prodotto_detail_response(self):
    #     response = self.client.get(reverse('prodotto:prodotto-detail', args=[1]))
    #     self.assertEqual(response.status_code, 200)


class TestModels(TestCase):

    def setUp(self):
        self.prodotto = Prodotto.objects.create(
            titolo='esempio esempio',
            id_prodotto=1,
            descrizione='prova',
            prezzo=10,
            ricambio='ri',
            marca='p',

        )

    def test_default_n_acquisti(self):
        self.assertEqual(self.prodotto.n_acquisti, 0)
