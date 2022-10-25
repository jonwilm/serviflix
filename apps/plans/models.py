from django.db import models


class TimeDiscount(models.Model):
    time = models.CharField('Tiempo', max_length=50, help_text='Tiempo a pagar')
    discount_rate = models.FloatField('Porcentaje de descuento', default=0, blank=False, null=False, help_text='(%)')

    def __str__(self):
        return self.time

    class Meta():
        verbose_name = 'Cuota'
        verbose_name_plural = 'Cuotas'


class Plan(models.Model):
    name = models.CharField('Nombre del plan', max_length=100, blank=False, null=False)
    price = models.FloatField('Precio del plan', default=0)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Plan'
        verbose_name_plural = 'Planes'