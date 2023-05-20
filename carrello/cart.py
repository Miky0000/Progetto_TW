from django.conf import settings
from django.shortcuts import redirect


class Cart(object):

    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # salvataggio carrello vuoto nella sessione
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, action=None):
        """
        aggiungiamo un prodotto o una quantità
        """
        id = product.id
        newItem = True
        if str(product.id) not in self.cart.keys():

            self.cart[product.id] = {
                'userid': self.request.user.id,
                'product_id': id,
                'name': product.titolo,
                'quantity': 1,
                'price': str(product.prezzo),
                'image': product.img.url
            }
        else:
            newItem = True

            for key, value in self.cart.items():
                if key == str(product.id):
                    value['quantity'] = value['quantity'] + 1
                    newItem = False
                    self.save()
                    break
            if newItem == True:
                self.cart[product.id] = {
                    'userid': self.request,
                    'product_id': product.id,
                    'name': product.titolo,
                    'quantity': 1,
                    'price': str(product.prezzo),
                    'image': product.img.url
                }

        self.save()

    def save(self):
        # aggiornamento carrello session
        self.session[settings.CART_SESSION_ID] = self.cart
        # settiamo modified a true cosi siamo sicuri che verrà salvato
        self.session.modified = True

    def remove(self, product):
        """
        rimuoviamo un prodotto
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def decrement(self, product):
        for key, value in self.cart.items():
            if key == str(product.id):

                value['quantity'] = value['quantity'] - 1
                if (value['quantity'] < 1):
                    return redirect('carrello:cart_detail')
                self.save()
                break
            else:
                print("errore")

    def clear(self):
        # carrello vuoto
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True
