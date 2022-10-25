# Django
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
# Apps
from apps.users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    MALE = 'M'
    FEMALE = 'F'

    GENDER_CHOICES = [
        (MALE, 'Masculino'),
        (FEMALE, 'Femenino'),
    ]

    DNI = 'D'
    PASSPORT = 'P'
    RNC = 'R'

    TYPE_DOC_CHOICES = [
        (DNI, 'DNI'),
        (PASSPORT, 'Pasaporte'),
        (RNC, 'RNC'),
    ]

    SUPERU = '1'
    EMPLOYEE = '2'
    CLIENT = '3'

    TYPE_USER = [
        (SUPERU, 'Super Usuario'),
        (EMPLOYEE, 'Empleado'),
        (CLIENT, 'Cliente'),
    ]

    first_name = models.CharField('Nombres', max_length=100, blank=False, null=False)
    last_name = models.CharField('Apellidos', max_length=100, blank=False, null=False)
    email = models.EmailField('Correo electronico', unique=True, blank=False, null=False)
    type_doc = models.CharField('Tipo de Documento', max_length=1, choices=TYPE_DOC_CHOICES, default='D', blank=False, null=False)
    n_doc = models.CharField('Numero de Documento', max_length=100, blank=False, null=False)
    address = models.TextField('Direccion', blank=False, null=False)
    phone = models.CharField('Telefono', max_length=100, blank=False, null=False)
    type_user = models.CharField('Tipo de Usuario', max_length=1, choices=TYPE_USER, default='3', blank=False, null=False)
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
