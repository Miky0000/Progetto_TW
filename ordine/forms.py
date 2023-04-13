from django import forms


class CheckoutForm(forms.Form):
    telefono = forms.IntegerField(max_value=9999999999, required=True, help_text=' 1234567890')
    indirizzo = forms.CharField(max_length=50, required=True, help_text=' via esempio 6')
    email = forms.CharField(max_length=120, help_text=' required')
    carta = forms.CharField(max_length=19, required=True, help_text=' 1111-2222-3333-4444')
    scadenza = forms.DateField(required=True, help_text=' yyyy-mm')
    cvv = forms.CharField(max_length=3, required=True, help_text=' CCC')
