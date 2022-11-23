from django.db import models


class TimeDiscount(models.Model):
    time = models.CharField('Plan', max_length=50, help_text='Tiempo a pagar')
    discount_rate = models.FloatField('Porcentaje de descuento', default=0, blank=False, null=False, help_text='(%)')

    def __str__(self):
        return self.time

    class Meta():
        verbose_name = 'Plan'
        verbose_name_plural = 'Planes'


class Plan(models.Model):
    name = models.CharField('Membresia', max_length=100, blank=False, null=False)
    price = models.FloatField('Precio', default=0)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Membresia'
        verbose_name_plural = 'Membresias'