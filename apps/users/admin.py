from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'type_user', 'password')}),
        (('Información Personal'), {
            'fields': (
                'first_name',
                'last_name',
                'type_doc',
                'n_doc',
                'address',
                'phone',
            )
        }),

        (('Permisos'), {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser'
            ),
        }),

        (('Fechas Importantes'), {
            'fields': (
                'last_login',
            )
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'type_user',
                'first_name',
                'last_name',
                'type_doc',
                'n_doc',
                'address',
                'phone',
                'password1',
                'password2'
            ),
        }),
    )
    
    list_display = ('email', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'email',)
    list_filter = ('type_user', 'is_staff', 'is_superuser')
    ordering = ('email', 'first_name', 'last_name', )


admin.site.register(User, UserAdmin)
