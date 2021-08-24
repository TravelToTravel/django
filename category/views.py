from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from category.models import Category


class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'
    context_object_name = 'category_list'
