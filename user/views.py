from django.contrib.auth import logout, login
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, UpdateView
from django.views.generic.base import TemplateResponseMixin

from user.forms import UserLoginForm, UserCreateForm, UserEditForm


class UserLoginView(FormView):
    form_class = UserLoginForm
    template_name = 'user/user_login_form.html'

    def form_valid(self, form):
        login(self.request, form.user)
        return redirect(self.request.GET.get('next', '/'))


class UserLogoutView(View):
    def get(self, request):
        logout(self.request)
        return redirect('/')


class UserCreateView(FormView):
    form_class = UserCreateForm
    template_name = 'user/user_create_form.html'

    def form_valid(self, form):
        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password1'],
        )
        login(self.request, user)
        return redirect('/')


class UserEditView(PermissionRequiredMixin, FormView):
    form_class = UserEditForm
    template_name = 'user/user_create_form.html'
    permission_required = "message.change_user"
    raise_exception = True

    def form_valid(self, form, pk):
        user = User.objects.create_user(
            pk=pk,
            username = form.cleaned_data['username'],
            first_name = form.cleaned_data['first_name'],
            last_name = form.cleaned_data['last_name'],
        )
        login(self.request, user)
        return redirect('/')
    # success_url = reverse_lazy('tweet-list')
    # permission_required = "user.change_user"
    # raise_exception = True
