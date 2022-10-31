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


@admin.action(description='Marcar seleccionados como PUBLICADOS')
def make_published(modeladmin, request, queryset):
    queryset.update(state=True)

@admin.action(description='Marcar seleccionados como NO PUBLICADOS')
def make_not_published(modeladmin, request, queryset):
    queryset.update(state=False)

class ServiceAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('state', 'user', 'category', 'title', 'company', 'plan', 'cuota',)}),
        (('INFORMACION'), {
            'fields': (
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
    list_display = ('id', 'title', 'category', 'user', 'state',)
    search_fields = ('category', 'title',)
    list_filter = ('state', 'category',)
    ordering = ('date_create',)
    readonly_fields = ('date_mod', 'date_create',)
    actions = [make_published, make_not_published]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Service, ServiceAdmin)
