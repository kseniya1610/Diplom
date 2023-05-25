from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from .forms import *
from silant.models import ServiceCompany
from .models import *


class AccountList(PermissionRequiredMixin, ListView):
    permission_required = 'auth.view_user'
    model = User
    template_name = 'account_list.html'
    context_object_name = 'users'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        order_by = self.request.GET.get('order_by', 'first_name')
        context['users'] = User.objects.order_by(order_by)
        return context


class AccountItem(PermissionRequiredMixin, DetailView):
    permission_required = 'auth.view_user'
    model = User
    template_name = 'user_item.html'
    context_object_name = 'user_item'


class CreateAccount(PermissionRequiredMixin, CreateView):
    permission_required = 'auth.add_user'
    model = User
    template_name = 'create_user.html'
    form_class = CreateAccountForm
    success_url = '/accounts/account_list'

    def form_valid(self, form):
        group = form.cleaned_data.get("groups")
        first_name = form.cleaned_data.get("first_name")
        username = form.cleaned_data.get("username")
        user = form.save()
        id = User.objects.get(username=username).id
        user.password = make_password(form.cleaned_data.get("password"))
        user.save()
        if group.filter(name='service').exists():
            object = ServiceCompany(user_id=id, name=first_name, description="Отсутствует")
            object.save()
        return super().form_valid(form)


class EditAccount(PermissionRequiredMixin, UpdateView):
    permission_required = 'auth.change_user'
    model = User
    template_name = 'update_user.html'
    form_class = UpdateAccountForm
    success_url = '/accounts/account_list'

    def form_valid(self, form):
        form.save()
        group = form.cleaned_data.get("groups")
        first_name = form.cleaned_data.get("first_name")
        username = form.cleaned_data.get("username")
        id = User.objects.get(username=username).id
        if ServiceCompany.objects.filter(user_id=id).exists():
            service_company = ServiceCompany.objects.get(user_id=id)
            service_company.name = first_name
            service_company.save()
        if group.filter(name='service').exists() and not ServiceCompany.objects.filter(user_id=id).exists():
            object = ServiceCompany(user_id=id, name=first_name, description="Отсутствует")
            object.save()
        return super().form_valid(form)
