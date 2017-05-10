from django import template
from customer2.models import PurchaseRecord

register = template.Library()

@register.assignment_tag
def has_buyed(user, note, buy_for):

    if buy_for not in ['lp', 'nlp', 'bs', 'wdp',]:
        return False

    if not PurchaseRecord.objects.filter(
        buyer=user, 
        buy_note=note,
        buy_for=buy_for):
        return False
    return True