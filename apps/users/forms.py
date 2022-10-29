from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

from apps.users.models import User


class LoginForm(forms.Form):
    email = forms.CharField(
        label='Correo Electronico',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Correo Electronico',
            }
        )
    )
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña'
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


doc_type = [
    ('D', 'DNI'),
    ('P', 'Pasaporte'),
    ('R', 'RNC'),
]

class RegisterForm(forms.Form):
    email = forms.EmailField(
        label='Correo Electronico',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Correo Electronico',
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
            password=pw,
            defaults={}
        )


class UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'type_doc', 'n_doc', 'address', 'phone']
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'type_doc': forms.Select(
                choices=doc_type,
                attrs={
                    'class': 'form-select',
                    'style': 'width: 30%;',
                }
            ),
            'n_doc': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'style': 'width: 70%;',
                }
            ),
            'address': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '2',
                    'style': 'resize: none;'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
