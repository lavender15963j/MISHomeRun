from django import template

from customer.models import FakeNote

register = template.Library()

@register.assignment_tag
def has_fake_note(user, betting):
    if not FakeNote.objects.filter(user=user, betting=betting):
        return None
    return FakeNote.objects.get(user=user, betting=betting)