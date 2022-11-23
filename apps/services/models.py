from distutils.command.upload import upload
import email
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


STATUS_CHOICES = [
    ('Inactivo', 'Inactivo'),
    ('Activo', 'Activo'),
    ('En revisión', 'En revisión'),
    ('Pausado', 'Pausado'),
]

class Service(models.Model):
    status = models.CharField(
        'Estado', max_length=20, choices=STATUS_CHOICES, default='En revisión'
    )
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name='Usuario'
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, verbose_name='Categoria'
    )
    title = models.CharField(
        'Titulo', max_length=100
    )
    company = models.CharField(
        'Empresa', max_length=150, blank=True, null=True
    )
    slug = models.SlugField(
        'URL', max_length=255, unique=True
    )
    plan = models.ForeignKey(
        Plan, on_delete=models.PROTECT, verbose_name='Plan'
    )
    cuota = models.ForeignKey(
        TimeDiscount, on_delete=models.PROTECT, verbose_name='Cuota'
    )
    # Contenido
    logo = models.ImageField(
        'Logo', upload_to='media/services/logos', default='static/img/defaults/service_logo.jpg', help_text='Logo del servicio o empresa'
    )
    image = models.ImageField(
        'Imagen', upload_to='media/services/covers', default='static/img/defaults/service_cover.jpg', help_text='Imagen de Portada'
    )
    description = models.TextField(
        'Descripción', blank=True, null=True, help_text='Descripcion de servicios ofrecidos'
    )
    # Ubicación 
    address = models.CharField(
        'Dirección', max_length=255, blank=True, null=True
    )
    lat = models.CharField(
        'Latitud', max_length=50, blank=True, null=True
    )
    lng = models.CharField(
        'Longitud', max_length=50, blank=True, null=True
    )
    # Contacto
    email = models.EmailField(
        'Email', blank=True, null=True
    )
    phone1 = models.CharField(
        'Telefono 1', max_length=12, blank=True, null=True, help_text=541234567890
    )
    phone2 = models.CharField(
        'Telefono 2', max_length=12, blank=True, null=True, help_text=541234567890
    )
    whatsapp = models.CharField(
        'Whatsapp', max_length=12, blank=True, null=True, help_text=541234567890
    )
    web = models.URLField(
        'Web', blank=True, null=True
    )
    # Horario de atención
    office_hours = models.TextField(
        'Horario de Atención', blank=True, null=True
    )
    # Fechas
    date_mod = models.DateField(
        'Ultima Actualización', auto_now=True, auto_now_add=False
    )
    date_create = models.DateField(
        'Fecha de creación', auto_now=False, auto_now_add=True
    )

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


SOCIAL_NETWORK_CHOICES = [
    ('Facebook', 'Facebook'),
    ('Twitter', 'Twitter'),
    ('Instagram', 'Instagram'),
    ('Youtube', 'Youtube'),
    ('Messenger', 'Messenger'),
    ('Telegram', 'Telegram'),
]

class SocialNetwork(models.Model):
    name = models.CharField('Red Social', max_length=50, choices=SOCIAL_NETWORK_CHOICES)
    url = models.URLField('URL')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Servicio')

    class Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'

    def __str__(self):
        return self.name


PAYMETHODS = [
    ('Efectivo', 'Efectivo'),
    ('Visa', 'Visa'),
    ('Mastercard', 'Mastercard'),
    ('Mercado Pago', 'Mercado Pago'),
]

class PaymentMethods(models.Model):
    paymethod = models.CharField('Metodo de Pago', max_length=50, choices=PAYMETHODS)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Servicio')

    class Meta:
        verbose_name = 'Metodo de Pago'
        verbose_name_plural = 'Metodos de Pagos'

    def __str__(self):
        return self.paymethod
