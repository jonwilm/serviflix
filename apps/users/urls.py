# Django
from django.urls import path

# Apps
from . import views

app_name = "users_app"

urlpatterns = [
    path(
        'login',
        views.LoginUser.as_view(),
        name='user-login',
    ),
    path(
        'logout',
        views.LogoutView.as_view(),
        name='user-logout',
    ),
    path(
        'register',
        views.RegisterUser.as_view(),
        name='user-register',
    ),
    path(
        'user/profile',
        views.ProfileUser.as_view(),
        name='user-profile',
    ),
    path(
        'user/change-password',
        views.ChangePasswordUser.as_view(),
        name='user-change-password',
    ),
]
