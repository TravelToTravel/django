from django.urls import path

from category.views import CategoryListView

app_name = 'categories'

urlpatterns = [
    path('list', CategoryListView.as_view(), name='list'),
]
