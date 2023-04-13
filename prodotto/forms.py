from django import forms
from .models import Prodotto


class ProdottoForm(forms.ModelForm):
    class Meta:
        model = Prodotto
        fields = (
            'id_prodotto', 'prezzo', 'marca', 'modello', 'anno', 'descrizione', 'venditore',)
