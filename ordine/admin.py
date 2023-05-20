from django.contrib import admin
from .models import Ordine, Contattaci, Recensione, Rimborsi
from django.core.mail import send_mail


@admin.register(Ordine)
class OrdineAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'spedito', 'restituito', 'user', 'prodotto','prod_id', 'prezzo', 'quantity', 'totale', 'data')
    readonly_fields = ('spedito', 'restituito')
    actions = ['spedisci']

    @admin.action(description='spedisci ordine al cliente')
    def spedisci(self, request, queryset):
        for o in queryset:
            if not o.spedito:
                o.spedito = True
                o.save()
                send_mail(
                    'Spedizione Ordine',
                    'Ciao abbiamo effettuato la spedizione del tuo ordine, \n'
                    + o.prodotto + '\n'
                                   'prezzo: ' + str(o.prezzo) + '\n'
                                                                'qty: ' + str(o.quantity) + '\n'
                                                                                            'effettuato il: ' + str(
                        o.data) + '\n'
                                  'riceverai i nostri prodotti entro 4 giorni lavorativi.'
                                  'Grazie per averci scelto.',
                    request.user.email,
                    [o.email],
                    fail_silently=False,
                )


@admin.register(Contattaci)
class ContattacciAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'oggetto')


@admin.register(Recensione)
class RecensioneAdmin(admin.ModelAdmin):
    list_display = ('user', 'prodotto', 'valutazione', 'creata')


@admin.register(Rimborsi)
class RimborsiAdmin(admin.ModelAdmin):
    list_display = ('id', 'rimborsato', 'user', 'prodotto', 'prezzo', 'quantity', 'effettuato')
    readonly_fields = ('rimborsato',)
    actions = ['rimborsa']

    @admin.action(description='rimborsa ordine al cliente')
    def rimborsa(self, request, queryset):
        for o in queryset:
            if not o.rimborsato:
                o.rimborsato = True
                o.save()
                send_mail(
                    'Rimborso Ordine',
                    'Ciao abbiamo effettuato il rimborso del tuo ordine, \n'
                    + o.prodotto + '\n'
                                   'prezzo: ' + str(o.prezzo) + '\n'
                                                                'qty: ' + str(o.quantity) + '\n'
                                                                                            'effettuato il: ' + str(
                        o.effettuato) + '\n'
                                        'riceverai il rimborso entro 4 giorni lavorativi.'
                                        'Grazie per averci scelto.',
                    request.user.email,
                    [o.user.email],
                    fail_silently=False,
                )
