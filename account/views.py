from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from account.decorators import account_ownership_required
from account.forms import AccountUpdateForm

has_ownership = [account_ownership_required, login_required]


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:login')    # 회원가입시 로그인화면으로 이동
    template_name = 'account/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'account/list.html'


@method_decorator(has_ownership, 'post')
@method_decorator(has_ownership, 'get')
@method_decorator(account_ownership_required, 'get')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('festivals:main')
    template_name = 'account/update.html'


@method_decorator(has_ownership, 'post')
@method_decorator(has_ownership, 'get')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accounts:login')
    template_name = 'account/delete.html'
