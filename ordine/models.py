from django.db import models
from prodotto.models import Prodotto
from django.conf import settings

"""
class Ordine(models.Model):
    image = models.ImageField(upload_to="images/")
    prodotto = models.CharField(max_length=100)
    prod_id = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    prezzo = models.FloatField()
    quantity = models.IntegerField()
    totale = models.FloatField()
    indirizzo = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.IntegerField()
    data = models.DateTimeField()
    spedito = models.BooleanField(default=False)
    restituito = models.BooleanField(default=False)

    class Meta:
        ordering = ('-data',)

    def __str__(self):
        return str(self.id)
"""


class Ordine(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    prodotto = models.ForeignKey(Prodotto, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    totale = models.FloatField()
    indirizzo = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.IntegerField()
    data = models.DateTimeField()
    spedito = models.BooleanField(default=False)
    restituito = models.BooleanField(default=False)

    class Meta:
        ordering = ('-data',)

    def __str__(self):
        return str(self.id)


class Contattaci(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    oggetto = models.CharField(max_length=100)
    messaggio = models.TextField()

    def __str__(self):
        return self.nome


class Recensione(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    prodotto = models.ForeignKey(Prodotto, on_delete=models.CASCADE)
    commento = models.TextField(max_length=250)
    valutazione = models.IntegerField(default=0, null=True, blank=True)
    creata = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


"""
class Rimborsi(models.Model):
    image = models.ImageField(upload_to="images/")
    prodotto = models.CharField(max_length=100)
    prod_id = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    prezzo = models.FloatField()
    quantity = models.IntegerField()
    motivo = models.TextField(max_length=2000)
    effettuato = models.DateTimeField(auto_now_add=True)
    rimborsato = models.BooleanField(default=False)

    class Meta:
        ordering = ('-effettuato',)

    def __str__(self):
        return str(self.id)
"""


class Rimborsi(models.Model):
    ordine = models.ForeignKey(Ordine, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    motivo = models.TextField(max_length=2000)
    effettuato = models.DateTimeField(auto_now_add=True)
    rimborsato = models.BooleanField(default=False)

    class Meta:
        ordering = ('-effettuato',)

    def __str__(self):
        return str(self.id)
