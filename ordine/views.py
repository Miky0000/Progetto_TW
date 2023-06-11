import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from .models import Ordine, Contattaci, Recensione, Rimborsi
from prodotto.models import Prodotto
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

"""
@login_required
def Checkout(request):
    if request.method == "POST":
        indirizzo = request.POST.get("indirizzo")
        telefono = request.POST.get("telefono")
        email = request.POST.get("email")
        cart = request.session.get("cart")
        uid = request.session.get("_auth_user_id")
        user = User.objects.get(pk=uid)
        data = datetime.datetime.now()
        for i in cart:
            a = (float(cart[i]['price']))
            b = cart[i]['quantity']
            totale = a * b
            ordine = Ordine(
                user=user,
                prodotto=cart[i]['name'],
                prod_id=cart[i]['product_id'],
                prezzo=cart[i]['price'],
                quantity=cart[i]['quantity'],
                image=cart[i]['image'],
                indirizzo=indirizzo,
                telefono=telefono,
                email=email,
                totale=totale,
                data=data
            )
            ordine.save()
            p = Prodotto.objects.get(id=ordine.prod_id)
            p.n_acquisti += 1 * b
            p.save()
            send_mail(
                'Ricezione Ordine',
                'Ciao abbiamo preso in carico il tuo ordine, \n'
                + ordine.prodotto + '\n'
                                    'prezzo: ' + str(ordine.prezzo) + '\n'
                                                                      'qty: ' + str(ordine.quantity) + '\n'
                                                                                                       'effettuato il: ' + str(
                    ordine.data) + '\n'
                                   'riceverai un email non appena sarà pronto per essere spedito.',
                'from@example.com',
                [email],
                fail_silently=False,
            )

        messages.success(request, ' hai effettuato il tuo ordine con successo')
        request.session['cart'] = {}
        return redirect('prodotto:prodotto-list')
"""


@login_required
def Checkout(request):
    if request.method == "POST":
        indirizzo = request.POST.get("indirizzo")
        telefono = request.POST.get("telefono")
        email = request.POST.get("email")
        cart = request.session.get("cart")
        uid = request.session.get("_auth_user_id")
        user = User.objects.get(pk=uid)
        data = datetime.datetime.now()
        for i in cart:
            a = (float(cart[i]['price']))
            b = cart[i]['quantity']
            print(cart[i]['product_id'])
            totale = a * b
            ordine = Ordine(
                user=user,
                prodotto=Prodotto.objects.get(id=cart[i]['product_id']),
                quantity=cart[i]['quantity'],
                indirizzo=indirizzo,
                telefono=telefono,
                email=email,
                totale=totale,
                data=data
            )
            ordine.save()
            p = Prodotto.objects.get(id=ordine.prodotto.id)
            p.n_acquisti += 1 * b
            p.save()
            send_mail(
                'Ricezione Ordine',
                'Ciao abbiamo preso in carico il tuo ordine, \n'
                + ordine.prodotto.titolo + '\n'
                                           'prezzo: ' + str(ordine.prodotto.prezzo) + '\n'
                                                                                      'qty: ' + str(
                    ordine.quantity) + '\n'
                                       'effettuato il: ' + str(
                    ordine.data) + '\n'
                                   'riceverai un email non appena sarà pronto per essere spedito.',
                'from@example.com',
                [email],
                fail_silently=False,
            )

        messages.success(request, ' hai effettuato il tuo ordine con successo')
        request.session['cart'] = {}
        return redirect('prodotto:prodotto-list')


"""
@login_required
def Restituisci(request, id):
    ordine = Ordine.objects.get(id=id)
    if request.method == "POST":
        q = int(request.POST.get("quantity_input"))
        motivo = request.POST.get("motivo")
        if q and q <= ordine.quantity:
            rimborso = Rimborsi(
                image=ordine.image,
                prodotto=ordine.prodotto,
                prod_id=ordine.prod_id,
                user=ordine.user,
                prezzo=ordine.prezzo,
                quantity=q,
                motivo=motivo,
            )
            rimborso.save()
            ordine.quantity = ordine.quantity - q
            ordine.totale = ordine.quantity * ordine.prezzo
            if ordine.quantity == 0:
                ordine.restituito = True
            ordine.save()
            messages.success(request, ' hai effettuato il tuo reso con successo')
            send_mail(
                'Reso Ordine',
                'Ciao abbiamo preso in carico il tuo reso, \n'
                + ordine.prodotto + '\n'
                                    'prezzo: ' + str(ordine.prezzo) + '\n'
                                                                      'qty: ' + str(q) + '\n'
                                                                                         'effettuato il: ' + str(
                    ordine.data) + '\n'
                                   'riceverai un email non appena sarài rimborsato.',
                'from@example.com',
                [rimborso.user.email],
                fail_silently=False,
            )
        else:
            messages.error(request, ' quantià o motivo del reso non corretti')
            return redirect("ordine:restituisci-page", id=id)
        return redirect("ordine:ordine-list")
    return render(request, 'ordine/restituisci.html', {'object': ordine})
"""


@login_required
def Restituisci(request, id):
    ordine_ref = Ordine.objects.get(id=id)
    if request.method == "POST":
        q = int(request.POST.get("quantity_input"))
        motivo = request.POST.get("motivo")
        if q and q <= ordine_ref.quantity:
            rimborso = Rimborsi(
                ordine=ordine_ref,
                quantity=q,
                motivo=motivo,
            )
            rimborso.save()
            ordine_ref.quantity = ordine_ref.quantity - q
            ordine_ref.totale = ordine_ref.quantity * ordine_ref.prodotto.prezzo
            if ordine_ref.quantity == 0:
                ordine_ref.restituito = True
            ordine_ref.save()
            messages.success(request, ' hai effettuato il tuo reso con successo')
            send_mail(
                'Reso Ordine',
                'Ciao abbiamo preso in carico il tuo reso, \n'
                + ordine_ref.prodotto.titolo + '\n'
                                               'prezzo: ' + str(ordine_ref.prodotto.prezzo) + '\n'
                                                                                              'qty: ' + str(q) + '\n'
                                                                                                                 'effettuato il: ' + str(
                    ordine_ref.data) + '\n'
                                       'riceverai un email non appena sarài rimborsato.',
                'from@example.com',
                [rimborso.ordine.user.email],
                fail_silently=False,
            )
        else:
            messages.error(request, ' quantià o motivo del reso non corretti')
            return redirect("ordine:restituisci-page", id=id)
        return redirect("ordine:ordine-list")
    return render(request, 'ordine/restituisci.html', {'object': ordine_ref})


@login_required
def Contatto(request):
    if request.method == 'POST':
        contatto = Contattaci(
            nome=request.POST.get('nome'),
            email=request.POST.get('email'),
            oggetto=request.POST.get('oggetto'),
            messaggio=request.POST.get('messaggio'),
        )
        contatto.save()
        messages.success(request, ' hai inviato il tuo messaggio con successo')
        return redirect('homepage:home')
    return render(request, 'contatto/contatto.html')


@login_required
def RecensioneView(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        prodotto = Prodotto.objects.get(id=prod_id)
        commento = request.GET.get('commento')
        valutazione = request.GET.get('valutazione')
        user = request.user
        Recensione(user=user, prodotto=prodotto, commento=commento, valutazione=valutazione).save()
        messages.success(request, ' hai inviato la tua recensione con successo')
        return redirect('ordine:ordine-list')


@method_decorator(login_required, name='dispatch')
class OrdineListView(ListView):
    model = Ordine
    paginate_by = 3
    template_name = 'ordine/ordine_list.html'

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = Ordine.objects.filter(user=user_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prodotti_all'] = Prodotto.objects.all()
        return context


"""
@method_decorator(login_required, name='dispatch')
class RimborsiListView(ListView):
    model = Rimborsi
    paginate_by = 3
    template_name = 'ordine/rimborsi_list.html'

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = Rimborsi.objects.filter(user=user_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prodotti_all'] = Prodotto.objects.all()
        return context
"""


@method_decorator(login_required, name='dispatch')
class RimborsiListView(ListView):
    model = Rimborsi
    paginate_by = 3
    template_name = 'ordine/rimborsi_list.html'

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = Rimborsi.objects.filter(ordine__user=user_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prodotti_all'] = Prodotto.objects.all()
        return context
