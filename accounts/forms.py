import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class DateInput(forms.DateInput):
    input_type = 'date'


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=False, help_text=' optional')
    last_name = forms.CharField(max_length=50, required=False, help_text=' optional')
    birthday = forms.DateField(required=False, help_text=' optional', widget=DateInput)
    email = forms.CharField(max_length=120, help_text=' required')

    def clean(self):
        cleaned_data = super().clean()
        birthday = cleaned_data.get('birthday')
        if birthday:
            if birthday.year >= datetime.datetime.now().year - 18:
                self.add_error('birthday', 'data non valida devi essere maggiorenne')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'birthday', 'email', 'password1', 'password2')


class UserModificaForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileModificaForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        birthday = cleaned_data.get('birthday')
        if birthday:
            if birthday.year >= datetime.datetime.now().year - 18:
                self.add_error('birthday', 'data non valida devi essere maggiorenne')

    class Meta:
        model = Profile
        widgets = {'birthday': DateInput()}
        fields = ('birthday',)
