from django import template

register = template.Library()


@register.filter()
def filtra_ordine(value, id):
    return value.filter(user=id)


@register.filter()
def meno(value, arg):
    value = int(value) - arg
    return value
