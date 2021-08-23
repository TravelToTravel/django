from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from review.decorators import question_ownership_required
from review.forms import ReviewCreationForm
from review.models import Review


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewCreationForm
    template_name = 'review/create.html'

    def form_valid(self, form):
        temp_review = form.save(commit=False)
        temp_review.writer = self.request.user
        temp_review.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('reviews:list')


class ReviewDetailView(DetailView):
    model = Review
    context_object_name = 'target_review'
    template_name = 'review/detail.html'


@method_decorator(question_ownership_required, 'get')
@method_decorator(question_ownership_required, 'post')
class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewCreationForm
    context_object_name = 'target_review'
    template_name = 'review/update.html'
    success_url = reverse_lazy('reviews:list')


@method_decorator(question_ownership_required, 'get')
@method_decorator(question_ownership_required, 'post')
class ReviewDeleteView(DeleteView):
    model = Review
    context_object_name = 'target_review'
    template_name = 'review/delete.html'
    success_url = reverse_lazy('reviews:list')


class ReviewListView(ListView):
    model = Review
    context_object_name = 'review_list'
    template_name = 'review/list.html'
    paginate_by = 10

