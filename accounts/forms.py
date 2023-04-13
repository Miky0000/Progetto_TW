from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=False, help_text=' optional')
    last_name = forms.CharField(max_length=50, required=False, help_text=' optional')
    birthday = forms.DateField(required=False, help_text=' yyyy-mm-dd')
    email = forms.CharField(max_length=120, help_text=' required')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'birthday', 'email', 'password1', 'password2')


class UserModificaForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileModificaForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('birthday',)
