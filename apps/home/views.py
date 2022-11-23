from django.views.generic import TemplateView
from apps.services.models import Service


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        services_pub = Service.objects.filter(status='Activo')
        context = {
            'services_pub': services_pub,
        }
        return context
