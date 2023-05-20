import datetime

from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class CheckoutForm(forms.Form):
    telefono = forms.IntegerField(max_value=9999999999, min_value=1000000000, required=True, help_text=' 1234567890')
    indirizzo = forms.CharField(max_length=50, required=True, help_text=' via esempio 6')
    email = forms.EmailField(max_length=120, help_text=' required')
    carta = forms.IntegerField(max_value=9999999999999999, min_value=1000000000000000, required=True, help_text=' 1111222233334444')
    scadenza = forms.DateField(required=True, widget=DateInput)
    cvv = forms.IntegerField(max_value=999, min_value=100, required=True, help_text=' 888')

    def clean(self):
        cleaned_data = super().clean()
        scadenza = cleaned_data.get('scadenza')
        if scadenza:
            if scadenza.year <= datetime.datetime.now().year:
                self.add_error('scadenza', 'data scadenza non valida')

