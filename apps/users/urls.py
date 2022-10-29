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
        'user/dashboard',
        views.DashboardUser.as_view(),
        name='user-dashboard',
    ),
    path(
        'user/update',
        views.UpdateUser.as_view(),
        name='user-update',
    ),
    path(
        'user/<int:pk>/delete',
        views.DeleteUser.as_view(),
        name="user-delete"),
    path(
        'user/change-password',
        views.ChangePasswordUser.as_view(),
        name='user-change-password',
    ),
]
