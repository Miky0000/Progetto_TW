from django.views.generic import TemplateView
from prodotto.models import Prodotto
from ordine.models import Recensione


class HomeView(TemplateView):
    template_name = 'homepage/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        piu_venduti = Prodotto.objects.all().order_by('-n_acquisti', '-modificato')
        context['piu_venduti'] = piu_venduti[0:6]
        context['recensioni_count'] = Recensione.objects.all()
        context['categorie'] = Prodotto.categorie
        return context
