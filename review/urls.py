from django.urls import path

from review.views import ReviewListView, ReviewCreateView, ReviewDetailView, ReviewUpdateView, ReviewDeleteView

app_name = 'reviews'

urlpatterns = [
    path('list', ReviewListView.as_view(), name='list'),

    path('create', ReviewCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ReviewDetailView.as_view(), name='detail'),
    path('update/<int:pk>', ReviewUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ReviewDeleteView.as_view(), name='delete'),
]
