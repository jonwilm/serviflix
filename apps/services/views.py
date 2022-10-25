# Django
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, FormView, UpdateView

from apps.users.models import User
from .models import Service
from .forms import RegisterServiceForm


class RegisterService(LoginRequiredMixin, CreateView):
    model = Service
    form_class = RegisterServiceForm
    template_name = 'services/register.html'
    success_url = reverse_lazy('users_app:user-profile')

    def post(self, request, *args, **kwargs):
        form = RegisterServiceForm(request.POST, user=self.request.user)
        print(request.POST)
        if form.is_valid():
            Service.objects.create(
                # user=user,
                category=self.request.POST['category'],
                title=self.request.POST['title'],
                company=self.request.POST['company'],
                plan=self.request.POST['plan'],
                cuota=self.request.POST['cuota'],
                image=self.request.POST['image'],
                description=self.request.POST['description'],
                address=self.request.POST['address'],
                phone1=self.request.POST['phone1'],
                phone2=self.request.POST['phone2'],
                whatsapp=self.request.POST['whatsapp'],
                office_hours=self.request.POST['office_hours'],
            )
        # return super(RegisterService, self).form_valid(form)
        return HttpResponseRedirect(reverse('users_app:user-profile'))
