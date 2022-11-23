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
        'registro',
        views.RegisterUser.as_view(),
        name='user-register',
    ),
    path(
        'usuario/perfil',
        views.DashboardUser.as_view(),
        name='user-dashboard',
    ),
    path(
        'usuario/actualizar-datos',
        views.UpdateUser.as_view(),
        name='user-update',
    ),
    path(
        'usuario/<int:pk>/eliminar',
        views.DeleteUser.as_view(),
        name="user-delete"),
    path(
        'usuario/cambiar-contraseña',
        views.ChangePasswordUser.as_view(),
        name='user-change-password',
    ),
]
