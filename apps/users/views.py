# Django
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.views.generic.edit import FormView, UpdateView
from django.forms import *
from django.contrib.auth.forms import PasswordChangeForm

from apps.users.models import User

from .forms import LoginForm, RegisterForm, ProfileForm


class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:home')

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


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "users/profile.html"
    success_message = "Datos Actualizados con exito"

    # def get_dispatch(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('users_app:user-profile')


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


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login'
            )
        )
