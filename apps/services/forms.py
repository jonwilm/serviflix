from django import forms
from django.forms import inlineformset_factory, modelformset_factory
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

from apps.services.models import Service, SocialNetwork, PaymentMethods


class RegisterServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            'category', 'title', 'company', 'plan', 'cuota',
            'logo', 'image', 'description',
            'address', 'email', 'phone1', 'phone2', 'whatsapp', 'web', 'office_hours',
        ]
        widgets = {
            'category': forms.Select(
                attrs={
                    'class': 'form-control',
                    'data-choices': '{"searchEnabled":true, "allowHTML":true,"itemSelectText":""}',
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
            'plan': forms.RadioSelect(
                attrs={
                    'class': 'form-check-input',
                    # 'data-choices': '{"searchEnabled":true, "allowHTML":true,"itemSelectText":""}',
                }
            ),
            'cuota': forms.Select(
                attrs={
                    'class': 'form-select',
                    # 'data-choices': '{"searchEnabled":true, "allowHTML":true,"itemSelectText":""}',
                }
            ),
            'logo': forms.FileInput(
                attrs={
                    'class': 'form-control',
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
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo electronico'
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
            'web': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Pagina Web'
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


class UpdateServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            'category', 'title', 'company', 'plan', 'cuota',
            'logo', 'image', 'description',
            'address', 'email', 'phone1', 'phone2', 'whatsapp', 'web', 'office_hours',
        ]
        widgets = {
            'category': forms.Select(
                attrs={
                    'class': 'form-control',
                    'data-choices': '{"searchEnabled":true, "allowHTML":true,"itemSelectText":""}',
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
                    'class': 'form-control',
                    'data-choices': '{"searchEnabled":true, "allowHTML":true,"itemSelectText":""}',
                }
            ),
            'cuota': forms.Select(
                attrs={
                    'class': 'form-control',
                    'data-choices': '{"searchEnabled":true, "allowHTML":true,"itemSelectText":""}',
                }
            ),
            'logo': forms.FileInput(
                attrs={
                    'class': 'form-control',
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
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo electronico'
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
            'web': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Pagina Web'
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


class SocialServiceForm(forms.ModelForm):
    class Meta:
        model = SocialNetwork
        fields = ('name', 'url',)

        widgets = {
            'name': forms.Select(
                attrs={
                    'class': 'form-control',
                    'data-choices': '{"searchEnabled":true, "allowHTML":true,"itemSelectText":""}',
                }
            ),
            'url': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Url'
                }
            ),
        }


SocialServiceFormSet = modelformset_factory(
    SocialNetwork,
    form=SocialServiceForm,
    extra=0,
    can_delete=True,
)


class PaymentMethodsServicesForm(forms.ModelForm):
    class Meta:
        model = PaymentMethods
        fields = ('paymethod',)

        widgets = {
            'paymethod': forms.Select(
                attrs={
                    'class': 'form-control',
                    'data-choices': '{"searchEnabled":true, "allowHTML":true,"itemSelectText":""}',
                }
            ),
        }


PaymentMethodsServicesFormSet = modelformset_factory(
    PaymentMethods,
    form=PaymentMethodsServicesForm,
    extra=0,
    can_delete=True,
)
