from django.views.generic import DetailView, ListView
from .models import Prodotto
from ordine.models import Recensione, Ordine


def comp(id):
    ordini_det = Ordine.objects.filter(prodotto__id=id)
    for x in ordini_det:
        ordini_dat = Ordine.objects.filter(data=x.data)
        if len(ordini_dat) > 1:
            comprati = list(())
            for y in ordini_dat:
                comprati.append(Prodotto.objects.get(id=y.prodotto.id))
            comprati.remove(Prodotto.objects.get(id=id))
            return comprati[:4]


class ProdottoDetailView(DetailView):
    model = Prodotto
    template_name = 'prodotto/prodotto_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recensioni = Recensione.objects.filter(prodotto=self.get_object().id).order_by('-creata')
        correlati = Prodotto.objects.filter(ricambio=self.get_object().ricambio).exclude(id=self.get_object().id)
        context["recensioni"] = recensioni[:5]
        context['recensioni_count'] = Recensione.objects.all()
        context["correlati"] = correlati[0:6]
        context["comprati_spesso"] = comp(self.get_object().id)

        return context


class ProdottoListView(ListView):
    model = Prodotto
    paginate_by = 3
    template_name = 'prodotto/prodotto_list.html'

    def get_queryset(self):
        tag = self.kwargs.get('categoria_tag', None)
        if tag:
            queryset = Prodotto.objects.filter(categoria__in=[tag])
        else:
            queryset = Prodotto.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recensioni_count'] = Recensione.objects.all()
        return context


class CercaView(ListView):
    model = Prodotto
    paginate_by = 3
    template_name = 'prodotto/cerca.html'

    def get_queryset(self):
        query = self.request.GET.get("query", False)
        queryset = Prodotto.objects.filter(titolo__icontains=query).order_by("-modificato")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recensioni_count'] = Recensione.objects.all()
        context['query'] = self.request.GET.get("query", False)
        return context
