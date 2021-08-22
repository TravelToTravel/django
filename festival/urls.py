from django.urls import path

from festival.views import FestivalListView

app_name = 'festivals'

urlpatterns = [
    path('main/', FestivalListView.as_view(), name='main'),
]
