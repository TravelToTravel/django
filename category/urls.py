from django.urls import path

from category import views
from category.views import PartyListView, AgeListView, LocationListView, PurposeListView

app_name = 'categories'

urlpatterns = [
    path('list1', PartyListView.as_view(), name='list1'),
    path('next', AgeListView.as_view(), name='next'),
    path('list3', LocationListView.as_view(), name='list3'),
    path('list4', PurposeListView.as_view(), name='list4'),
    # path('result', views.result, name='result'),
]
