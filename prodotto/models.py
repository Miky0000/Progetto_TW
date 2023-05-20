from django.conf import settings
from django.db import models
from django.urls import reverse


class Prodotto(models.Model):
    DUE_RUOTE = 'DR'
    TRE_RUOTE = 'TR'
    QUATTRO_RUOTE = 'QR'
    ALTRO = 'AL'
    categorie = [
        (DUE_RUOTE, 'DUE RUOTE'),
        (TRE_RUOTE, 'TRE RUOTE'),
        (QUATTRO_RUOTE, 'QUATTRO RUOTE'),
        (ALTRO, 'ALTRO'),
    ]
    categoria = models.CharField(max_length=2, choices=categorie, default='AL')
    titolo = models.CharField(max_length=100)
    id_prodotto = models.CharField(max_length=60)
    slug = models.SlugField()
    img = models.ImageField(upload_to="images/")
    descrizione = models.CharField(max_length=1000)
    prezzo = models.FloatField()
    ricambio = models.CharField(max_length=150)
    anno = models.IntegerField(blank=True, null=True)
    n_acquisti = models.IntegerField(default=0)
    marca = models.CharField(max_length=100)
    publicato = models.DateTimeField(auto_now_add=True)
    modificato = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-publicato',)

    def __str__(self):
        return self.titolo
