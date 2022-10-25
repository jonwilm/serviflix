from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

from apps.services.models import Service


class RegisterServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            'category', 'title', 'company', 'plan', 'cuota',
            'image', 'description',
            'address', 'phone1', 'phone2', 'whatsapp', 'office_hours',
        ]
        widgets = {
            'category': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Título'
                }
            ),
            'company': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Empresa'
                }
            ),
            'plan': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),
            'cuota': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descripción',
                    'rows': '3',
                    'style': 'resize: none;'
                }
            ),
            'address': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Dirección',
                    'rows': '2',
                    'style': 'resize: none;'
                }
            ),
            'phone1': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Teléfono 1'
                }
            ),
            'phone2': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Teléfono 2'
                }
            ),
            'whatsapp': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Whatsapp'
                }
            ),
            'office_hours': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Horario de Atención',
                    'rows': '2',
                    'style': 'resize: none;'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(RegisterServiceForm, self).__init__(*args, **kwargs)
