# Django
from django.urls import path

# Apps
from . import views

app_name = "services_app"

urlpatterns = [
    path(
        'services',
        views.ListService.as_view(),
        name='service-list',
    ),
    path(
        'services/register',
        views.RegisterService.as_view(),
        name='service-register',
    ),
    path(
        'services/<slug:slug>',
        views.DetailService.as_view(),
        name="service-detail"),
]
