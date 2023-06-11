from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .cart import Cart
from prodotto.models import Prodotto
from ordine.forms import CheckoutForm


@login_required
def cart_add(request, id):
    cart = Cart(request)
    product = Prodotto.objects.get(id=id)
    cart.add(product=product)
    messages.success(request, ' prodotto aggiunto al carrello con successo')
    if 'login' in request.META.get('HTTP_REFERER'):
        return redirect("homepage:home")
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def item_clear(request, id):
    cart = Cart(request)
    product = Prodotto.objects.get(id=id)
    cart.remove(product)
    return redirect("carrello:cart_detail")


@login_required
def item_increment(request, id):
    cart = Cart(request)
    product = Prodotto.objects.get(id=id)
    cart.add(product=product)
    return redirect("carrello:cart_detail")


@login_required
def item_decrement(request, id):
    cart = Cart(request)
    product = Prodotto.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("carrello:cart_detail")


@login_required
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("carrello:cart_detail")


@login_required
def cart_detail(request):
    form = CheckoutForm(request.POST)
    prodotti = Prodotto.objects.all()
    return render(request, 'carrello/cart_detail.html', {'form': form, 'prodotti': prodotti})
