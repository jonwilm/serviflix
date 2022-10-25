from django.contrib import admin
from django.db import models

from .models import TimeDiscount, Plan


class TimeDiscountAdmin(admin.ModelAdmin):
    list_display = ('time', 'discount_rate',)
    search_fields = ('time',)
    ordering = ('discount_rate', )


class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    search_fields = ('name',)
    ordering = ('price',)


admin.site.register(TimeDiscount, TimeDiscountAdmin)
admin.site.register(Plan, PlanAdmin)
