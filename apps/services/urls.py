# Django
from django.urls import path

# Apps
from . import views

app_name = "services_app"

urlpatterns = [
    path(
        'servicios',
        views.ListService.as_view(),
        name='service-list',
    ),
    path(
        'servicios/registro',
        views.RegisterService.as_view(),
        name='service-register',
    ),
    path(
        'servicios/<int:pk>/editar',
        views.UpdateService.as_view(),
        name='service-edit',
    ),
    path(
        'servicios/<slug:slug>',
        views.DetailService.as_view(),
        name="service-detail"),
]
