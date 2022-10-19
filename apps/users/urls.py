# Django
from django.urls import path

# Apps
from . import views

app_name = "users_app"

urlpatterns = [
    path(
        '',
        views.HomeView.as_view(),
        name='home',
    ),
    path(
        'login',
        views.LoginUser.as_view(),
        name='user-login',
    ),
    path(
        'register',
        views.RegisterUser.as_view(),
        name='user-register',
    ),
    path(
        'logout',
        views.LogoutView.as_view(),
        name='user-logout',
    ),
]
