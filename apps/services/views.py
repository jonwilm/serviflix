# Django
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from .models import PaymentMethods, Service, SocialNetwork
from .forms import RegisterServiceForm, UpdateServiceForm


class ListService(ListView):
    model = Service
    template_name = 'services/list.html'

    def get_context_data(self, **kwargs):
        services_all = super().get_context_data(**kwargs)
        services_pub = Service.objects.filter(state=True)
        context = {
            'services_all': services_all['object_list'],
            'services_pub': services_pub,
        }
        return context


class RegisterService(LoginRequiredMixin, CreateView):
    model = Service
    form_class = RegisterServiceForm
    template_name = 'services/register.html'
    success_url = reverse_lazy('users_app:user-dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateService(LoginRequiredMixin, UpdateView):
    model = Service
    form_class = UpdateServiceForm
    template_name = 'services/update.html'
    success_message = 'Datos Actualizados con exito'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('users_app:user-dashboard')

class DetailService(DetailView):
    model = Service
    template_name = 'services/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service = self.get_object()
        redes = SocialNetwork.objects.filter(service=service.pk)
        payMethods = PaymentMethods.objects.filter(service=service.pk)
        context = {
            'service': service,
            'redes': redes,
            'payMethods': payMethods,
        }
        return context
    
