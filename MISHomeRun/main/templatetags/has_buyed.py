from django import template
from customer.models import PurchaseRecord

register = template.Library()

@register.assignment_tag
def has_buyed(user, note, buy_for):

    b_lp = False
    b_nlp = False
    b_bsp = False
    b_wpd = False
    if buy_for == 'lp':
        b_lp = True
    elif buy_for == 'nlp':
        b_nlp = True
    elif buy_for == 'bs':
        b_bsp = True
    elif buy_for == 'wdp':
        b_wpd = True
    else:
        return False

    if not PurchaseRecord.objects.filter(
        buyer=user, 
        buy_note=note,
        b_lp=b_lp,
        b_nlp=b_nlp,
        b_bsp=b_bsp,
        b_wpd=b_wpd,):
        return False
    return True