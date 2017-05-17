from django.views.generic import UpdateView

from machina.apps.forum_member.views import ForumProfileUpdateView
from machina.core.db.models import get_model

class ForumProfileUpdateView(UpdateView):
    def get_success_url(self):
        return reverse('customer:profile')