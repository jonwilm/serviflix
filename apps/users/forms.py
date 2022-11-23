from random import choices
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, password_validation

from apps.users.models import User


class LoginForm(forms.Form):
    email = forms.CharField(
        label='Correo Electronico',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Correo Electronico',
                'autofocus': True
            }
        )
    )
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña',
            }
        )
    )

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError(
                'Email o Contraseña incorrectos'
            )

        return self.cleaned_data


TYPE_DOC_CHOICES = [
    ('', 'Seleccione...'),
    ('DNI', 'DNI'),
    ('CUIT', 'CUIT'),
    ('CUIL', 'CUIL'),
    ('PASSPORT', 'Pasaporte'),
]

PROVINCE_CHOICES = [
    ('', 'Seleccione...'),
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


class RegisterForm(forms.Form):
    email = forms.EmailField(
        label='Correo Electronico',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Correo Electronico',
                'autofocus': True,
            }
        )
    )
    first_name = forms.CharField(
        label='Nombre',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre'
            }
        )
    )
    last_name = forms.CharField(
        label='Apellido',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Apellido'
            }
        )
    )
    type_doc = forms.ChoiceField(
        label='Tipo de Documento',
        required=True,
        choices=TYPE_DOC_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-select ps-7',
                'placeholder': 'Tipo de documento',
                'style': 'width: 40%;'
            }
        )
    )
    n_doc = forms.CharField(
        label='Número de Documento',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Número de documento',
                'style': 'width: 60%;'
            }
        )
    )
    province = forms.ChoiceField(
        label='Provincia',
        required=True,
        choices=PROVINCE_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-select ps-7',
                'placeholder': 'Provincia'
            }
        )
    )
    location = forms.CharField(
        label='Localidad',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Localidad'
            }
        )
    )
    phone = forms.CharField(
        label='Teléfono',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Teléfono'
            }
        )
    )
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña',
            }
        )
    )
    repassword = forms.CharField(
        label='Confirme contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirme contraseña',
            }
        )
    )
    
    def clean(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('Correo electronico ya se encuentra registrado')

        pw1 = self.cleaned_data['password']
        pw2 = self.cleaned_data['repassword']
        if (pw1 != pw2):
            raise ValidationError('Confirmación de contraseña no concuerda')

    def save(self, *args, **kwargs):
        data = self.cleaned_data
        pw = make_password(data['password'])
        User.objects.get_or_create(
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            type_doc=data['type_doc'],
            n_doc=data['n_doc'],
            province=data['province'],
            location=data['location'],
            phone=data['phone'],
            password=pw,
            defaults={}
        )


class UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'type_doc', 'n_doc', 'province', 'location', 'phone']
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo electronico',
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellido',
                }
            ),
            'type_doc': forms.Select(
                attrs={
                    'class': 'form-select ps-7',
                    'style': 'width: 40%;',
                    'placeholder': 'Tipo de documento',
                }
            ),
            'n_doc': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'style': 'width: 60%;',
                    'placeholder': 'Número de documento',
                }
            ),
            'province': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Provincia',
                }
            ),
            'location': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Localidad',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Teléfono',
                }
            ),
        }
