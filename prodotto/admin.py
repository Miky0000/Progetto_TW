from django.contrib import admin
from .models import Prodotto


@admin.register(Prodotto)
class ProdottoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titolo', 'ricambio', 'categoria', 'modificato', 'n_acquisti', 'prezzo')
    prepopulated_fields = {'slug': ('titolo',)}
    search_fields = ('titolo', 'descrizione',)
    ordering = ('-modificato',)
    readonly_fields = ('n_acquisti',)
