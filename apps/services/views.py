# Django
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import PaymentMethods, Service, SocialNetwork, Category
from .forms import RegisterServiceForm, UpdateServiceForm, SocialServiceFormSet, PaymentMethodsServicesFormSet
from apps.plans.models import Plan, TimeDiscount


class ListService(ListView):
    model = Service
    template_name = 'services/list.html'

    def get_context_data(self, **kwargs):
        services_all = super().get_context_data(**kwargs)
        services_pub = Service.objects.filter(status='Activo')
        categories = Category.objects.all()
        context = {
            'services_all': services_all['object_list'],
            'services_pub': services_pub,
            'categories': categories,
        }
        return context


class RegisterService(LoginRequiredMixin, CreateView):
    form_class = RegisterServiceForm
    template_name = 'services/register.html'
    success_url = reverse_lazy('users_app:user-dashboard')

    def get_context_data(self, **kwargs):
        context = super(RegisterService, self).get_context_data(**kwargs)
        if "social_formset" not in context:
            context['social_formset'] = SocialServiceFormSet(
                queryset=SocialNetwork.objects.none(),
            )
        if "paymethod_formset" not in context:
            context['paymethod_formset'] = PaymentMethodsServicesFormSet(
                queryset=PaymentMethods.objects.none(),
            )
        context['porcents'] = TimeDiscount.objects.all()
        context['membership'] = Plan.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        social_formset = SocialServiceFormSet(request.POST)
        paymethod_formset = PaymentMethodsServicesFormSet(request.POST)
        if social_formset.is_valid() and paymethod_formset.is_valid() and form.is_valid():
            return self.form_valid(form, social_formset, paymethod_formset)
        else:
            return self.form_invalid(form, social_formset, paymethod_formset)

    def form_invalid(self, form, social_formset, paymethod_formset):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                social_formset=social_formset,
                paymethod_formset=paymethod_formset
            )
        )

    def form_valid(self, form, social_formset, paymethod_formset):
        service = form.save(commit=False)
        service.user = self.request.user
        service.save()
        instancesSocial = social_formset.save(commit=False)
        for instanceSocial in instancesSocial:
            instanceSocial.service = service
            instanceSocial.save()
        instancesPaymethod = paymethod_formset.save(commit=False)
        for instancePaymethod in instancesPaymethod:
            instancePaymethod.service = service
            instancePaymethod.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return str(self.success_url)


class UpdateService(LoginRequiredMixin, UpdateView):
    model = Service
    form_class = RegisterServiceForm
    template_name = 'services/update.html'
    success_url = reverse_lazy('users_app:user-dashboard')

    def get_context_data(self, **kwargs):
        context = super(UpdateService, self).get_context_data(**kwargs)
        if "social_formset" not in context:
            context['social_formset'] = SocialServiceFormSet(
                queryset=SocialNetwork.objects.filter(service=self.kwargs['pk']),
            )
        if "paymethod_formset" not in context:
            context['paymethod_formset'] = PaymentMethodsServicesFormSet(
                queryset=PaymentMethods.objects.filter(service=self.kwargs['pk']),
            )
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        social_formset = SocialServiceFormSet(
            request.POST,
            queryset=SocialNetwork.objects.filter(service=self.kwargs['pk']),
        )
        paymethod_formset = PaymentMethodsServicesFormSet(
            request.POST,
            queryset=PaymentMethods.objects.filter(service=self.kwargs['pk']),
        )
        if social_formset.is_valid() and paymethod_formset.is_valid() and form.is_valid():
            return self.form_valid(form, social_formset, paymethod_formset)
        else:
            return self.form_invalid(form, social_formset, paymethod_formset)

    def form_invalid(self, form, social_formset, paymethod_formset):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                social_formset=social_formset,
                paymethod_formset=paymethod_formset
            )
        )

    def form_valid(self, form, social_formset, paymethod_formset):
        self.object = form.save()
        instancesSocial = social_formset.save(commit=False)
        for instanceSocial in instancesSocial:
            instanceSocial.service = self.object
            instanceSocial.save()
        instancesPaymethod = paymethod_formset.save(commit=False)
        for instancePaymethod in instancesPaymethod:
            instancePaymethod.service = self.object
            instancePaymethod.save()

        if len(social_formset.deleted_objects) > 0:
            for obj in social_formset.deleted_objects:
                obj.delete()
        if len(paymethod_formset.deleted_objects) > 0:
            for obj in paymethod_formset.deleted_objects:
                obj.delete()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return str(self.success_url)

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
    

class DeleteService(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Service
    template_name = 'services/service_confirm_delete.html'
    success_url = reverse_lazy('users_app:user-dashboard')

    def test_func(self):
        user = self.get_object().user
        print(self.request.user)
        if self.request.user == user:
            return True
        return False

    def handle_no_permission(self):
        return HttpResponseRedirect(
            reverse(
                'users_app:user-dashboard'
            )
        )
