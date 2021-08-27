from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from category.models import Party, Age, Location, Purpose


class PartyListView(ListView):
    model = Party
    template_name = 'category/list.html'
    context_object_name = 'party_list'


class AgeListView(ListView):
    model = Age
    template_name = 'category/list.html'
    context_object_name = 'age_list'


class LocationListView(ListView):
    model = Location
    template_name = 'category/list.html'
    context_object_name = 'location_list'


class PurposeListView(ListView):
    model = Purpose
    template_name = 'category/list.html'
    context_object_name = 'purpose_list'
