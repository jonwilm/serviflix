# Django
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
# Apps
from apps.users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    
    TYPE_DOC_CHOICES = [
        ('DNI', 'DNI'),
        ('CUIT', 'CUIT'),
        ('CUIL', 'CUIL'),
        ('PASSPORT', 'Pasaporte'),
    ]

    SUPERU = '1'
    EMPLOYEE = '2'
    CLIENT = '3'

    TYPE_USER = [
        (SUPERU, 'Super Usuario'),
        (EMPLOYEE, 'Empleado'),
        (CLIENT, 'Cliente'),
    ]

    PROVINCE = [
        ('Buenos Aires', 'Buenos Aires'),
        ('Catamarca', 'Catamarca'),
        ('Chaco', 'Chaco'),
        ('Chubut', 'Chubut'),
        ('Córdoba', 'Córdoba'),
        ('Corrientes', 'Corrientes'),
        ('Entre Ríos', 'Entre Ríos'),
        ('Formosa', 'Formosa'),
        ('Jujuy', 'Jujuy'),
        ('La Pampa', 'La Pampa'),
        ('La Rioja', 'La Rioja'),
        ('Mendoza', 'Mendoza'),
        ('Misiones', 'Misiones'),
        ('Neuquén', 'Neuquén'),
        ('Río Negro', 'Río Negro'),
        ('Salta', 'Salta'),
        ('San Juan', 'San Juan'),
        ('San Luis', 'San Luis'),
        ('Santa Cruz', 'Santa Cruz'),
        ('Santa Fe', 'Santa Fe'),
        ('Santiago del Estero', 'Santiago del Estero'),
        ('Tierra del Fuego', 'Tierra del Fuego'),
        ('Tucumán', 'Tucumán'),
    ]

    first_name = models.CharField('Nombres', max_length=100)
    last_name = models.CharField('Apellidos', max_length=100)
    email = models.EmailField('Correo electronico', unique=True,)
    type_doc = models.CharField('Tipo de Documento', max_length=10, choices=TYPE_DOC_CHOICES)
    n_doc = models.CharField('Numero de Documento', max_length=100)
    province = models.CharField('Provincia', max_length=100, choices=PROVINCE)
    location = models.CharField('Localidad', max_length=100)
    phone = models.CharField('Telefono', max_length=100)
    type_user = models.CharField('Tipo de Usuario', max_length=1, choices=TYPE_USER, default='3')
    #
    is_staff = models.BooleanField('Staff', default=False, help_text='Indica que el usuario pertenece al staff de SERVIFLIX')
    is_active = models.BooleanField('Usuario Activo', default=True, help_text='Indica que el usuario esta activo en la plataforma')
    date_create = models.DateTimeField('Fecha de registro', auto_now_add=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    class Meta:

        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.email
