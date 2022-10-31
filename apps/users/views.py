# Django
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.views.generic import View, ListView, DetailView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.forms import *
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q

from apps.users.models import User
from apps.services.models import Service

from .forms import LoginForm, RegisterForm, UpdateForm


class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('users_app:user-dashboard')

    def form_valid(self, form):
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class RegisterUser(FormView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('users_app:user-login')

    def form_valid(self, form):
        form.save()
        return super(RegisterUser, self).form_valid(form)


class DashboardUser(LoginRequiredMixin, ListView):
    model = User
    template_name = 'users/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        services = Service.objects.filter(user=self.request.user)
        context['services'] = services
        return context


class UpdateUser(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UpdateForm
    template_name = 'users/update.html'
    success_message = 'Datos Actualizados con exito'

    def get_object(self, queryset=None):
        print(Service.objects.filter(user=self.request.user))
        return self.request.user

    def get_success_url(self):
        return reverse('users_app:user-dashboard')


class ChangePasswordUser(LoginRequiredMixin, FormView):
    template_name = 'users/change-password.html'
    model = User
    form_class = PasswordChangeForm

    def get_form(self, form_class=None):
        form = PasswordChangeForm(user=self.request.user)
        form.fields['old_password'].widget.attrs['class'] = 'form-control'
        form.fields['new_password1'].widget.attrs['class'] = 'form-control'
        form.fields['new_password2'].widget.attrs['class'] = 'form-control'
        form.fields['old_password'].widget.attrs['placeholder'] = 'Contraseña Actual'
        form.fields['new_password1'].widget.attrs['placeholder'] = 'Contraseña Nueva'
        form.fields['new_password2'].widget.attrs['placeholder'] = 'Confirmar Contraseña Nueva'
        return form

    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login'
            )
        )


class DeleteUser(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    success_url = '/'

    def test_func(self):
        user = self.get_object()
        if self.request.user == user:
            return True
        return False

    def handle_no_permission(self):
        return HttpResponseRedirect(
            reverse(
                'home_app:home'
            )
        )


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login'
            )
        )
