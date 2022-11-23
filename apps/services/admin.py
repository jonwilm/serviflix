from django.contrib import admin
from django.db import models

from .models import Category, Service, SocialNetwork, PaymentMethods


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name', )


class SocialNetworkAdmin(admin.TabularInline):
    model = SocialNetwork
    extra = 0


class PaymentMethodsAdmin(admin.TabularInline):
    model = PaymentMethods
    extra = 0


@admin.action(description='Marcar seleccionados como ACTIVOS')
def make_active(modeladmin, request, queryset):
    queryset.update(status='Activo')

@admin.action(description='Marcar seleccionados como INACTIVOS')
def make_inactive(modeladmin, request, queryset):
    queryset.update(status='Inactivo')

@admin.action(description='Marcar seleccionados como PAUSADOS')
def make_paused(modeladmin, request, queryset):
    queryset.update(status='Pausado')

class ServiceAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('status', 'user', 'category', 'title', 'company', 'plan', 'cuota',)}),
        (('INFORMACION'), {
            'fields': (
                'logo',
                'image',
                'description',
            )
        }),
        (('UBICACIÓN'), {
            'fields': (
                'address',
            )
        }),
        (('CONTACTO'), {
            'fields': (
                'email',
                'phone1',
                'phone2',
                'whatsapp',
                'web',
            )
        }),
        (('HORARIO DE ATENCIÓN'), {
            'fields': (
                'office_hours',
            )
        }),
        (('FECHAS IMPORTANTES'), {
            'fields': (
                'date_mod',
                'date_create',
            )
        }),
    )

    inlines = (SocialNetworkAdmin, PaymentMethodsAdmin)
    list_display = ('id', 'title', 'category', 'user', 'status',)
    search_fields = ('category', 'title',)
    list_filter = ('status', 'category',)
    ordering = ('date_create',)
    readonly_fields = ('date_mod', 'date_create',)
    actions = [make_active, make_inactive, make_paused]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(SocialNetwork)
