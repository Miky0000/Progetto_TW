from django import template

register = template.Library()


@register.filter()
def filtra(value, id):
    return value.filter(prodotto=id)
