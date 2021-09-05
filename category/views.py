from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView

from category.models import Party, Age, Location, Purpose


class PartyListView(ListView):
    model = Party
    template_name = 'category/list1.html'
    context_object_name = 'party_list'


class AgeListView(ListView):
    model = Age
    template_name = 'category/list2.html'
    context_object_name = 'age_list'


class LocationListView(ListView):
    model = Location
    template_name = 'category/list3.html'
    context_object_name = 'location_list'


class PurposeListView(ListView):
    model = Purpose
    template_name = 'category/list4.html'
    context_object_name = 'purpose_list'


# def result(request):
#     if request.method == 'POST':
#         party = request.POST.get('party')
#         if party == '#혼자':
#             new_party = Party()
#             new_party.text = party
#             new_party.save()
#             return HttpResponseRedirect(reverse('categories:result'))
#         else:
#
#             return HttpResponseRedirect(reverse('categories:result'))
#     else:
#         party_list = Party.objects.all()
#         return render(request, 'category/result.html', context={'party_list': party_list})
#



