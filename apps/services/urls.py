# Django
from django.urls import path

# Apps
from . import views

app_name = "services_app"

urlpatterns = [
    path(
        'services/register',
        views.RegisterService.as_view(),
        name='service-register',
    ),
]
