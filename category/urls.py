from django.urls import path

from category.views import PartyListView, AgeListView, LocationListView, PurposeListView

app_name = 'categories'

urlpatterns = [
    path('list', PartyListView.as_view(), name='list'),
    path('list', AgeListView.as_view(), name='list'),
    path('list', LocationListView.as_view(), name='list'),
    path('list', PurposeListView.as_view(), name='list'),
]
