from django.db import models
from django.utils.text import slugify

from apps.users.models import User
from apps.plans.models import Plan, TimeDiscount


class Category(models.Model):
    name = models.CharField('Nombre de la categoria', max_length=100, unique=True, blank=False, null=False)

    class Meta():
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class Service(models.Model):
    state = models.BooleanField('Publicado', default=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuario')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Categoria')
    title = models.CharField('Titulo', max_length=100)
    company = models.CharField('Empresa', max_length=150, blank=True, null=True)
    slug = models.SlugField('URL', max_length=255, unique=True)
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT, verbose_name='Plan')
    cuota = models.ForeignKey(TimeDiscount, on_delete=models.PROTECT, verbose_name='Cuota')

    # Contenido
    image = models.ImageField('Imagen', upload_to='media/services', blank=True, null=True, help_text='Imagen de Portada')
    description = models.TextField('Descripción', blank=True, null=True, help_text='Descripcion de servicios ofrecidos')

    # Ubicación y Contacto
    address = models.TextField('Dirección', blank=True, null=True)
    phone1 = models.CharField('Telefono 1', max_length=12, blank=True, null=True, help_text=541234567890)
    phone2 = models.CharField('Telefono 2', max_length=12, blank=True, null=True, help_text=541234567890)
    whatsapp = models.CharField('Whatsapp', max_length=12, blank=True, null=True, help_text=541234567890)
    office_hours = models.TextField('Horario de Atención', blank=True, null=True)

    # Fechas
    date_mod = models.DateField('Ultima Actualización', auto_now=True, auto_now_add=False)
    date_create = models.DateField('Fecha de creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def save(self, *args, **kwargs):
        super(Service, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = str(self.id) + '-' + slugify(self.title)
            self.save()

    def __str__(self):
        return self.title


class SocialNetwork(models.Model):
    name = models.CharField('Red Social', max_length=50)
    url = models.URLField('URL')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Servicio')

    class Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'


PAYMETHODS = [
    ('1', 'Efectivo'),
    ('2', 'Visa'),
    ('3', 'Mastercard'),
    ('4', 'Mercado Pago'),
]

class PaymentMethods(models.Model):
    paymethod = models.CharField('Metodo de Pago', max_length=2, choices=PAYMETHODS)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Servicio')

    class Meta:
        verbose_name = 'Metodo de Pago'
        verbose_name_plural = 'Metodos de Pagos'
