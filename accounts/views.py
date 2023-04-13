from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from prodotto.models import Prodotto
from ordine.models import Ordine, Recensione

from .forms import RegistrationForm, UserModificaForm, ProfileModificaForm


@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.user.id
        ultimo_ordine = Ordine.objects.filter(user=user_id).order_by('-data').first()
        if ultimo_ordine:
            ultimo_prodotto = Prodotto.objects.get(id=ultimo_ordine.prod_id)
            raccomandati = Prodotto.objects.filter(categoria=ultimo_prodotto.categoria).order_by('-modificato')
            context['raccomandati'] = raccomandati[0:3]
        else:
            context['raccomandati'] = []
        context['recensioni_count'] = Recensione.objects.all()
        return context


def Register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.birthday = form.cleaned_data.get("birthday")
            user.profile.save()
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            messages.success(request, ' hai creato il tuo profilo con successo')
            return redirect("accounts:profile")
    else:
        form = RegistrationForm()
    return render(request, "registration/registration.html", {'form': form})


@login_required
def Modifica(request):
    if request.method == 'POST':
        user_form = UserModificaForm(instance=request.user, data=request.POST)
        profile_form = ProfileModificaForm(instance=request.user.profile, data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ' hai modificato il tuo profilo con successo')
            return render(request, 'accounts/profile.html')
        else:
            messages.error(request, ' i dati non sono validi')
    else:
        user_form = UserModificaForm(instance=request.user)
        profile_form = ProfileModificaForm(instance=request.user.profile)
    return render(request, 'accounts/modifica.html', {'user_form': user_form, 'profile_form': profile_form})
