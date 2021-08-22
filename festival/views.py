
# Create your views here.
from django.views.generic import ListView

from festival.models import Festival


class FestivalListView(ListView):
    model = Festival
    template_name = 'festival/main.html'
    context_object_name = 'festival_list'
