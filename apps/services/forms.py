from django import forms
from django.forms import inlineformset_factory, modelformset_factory
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

from apps.services.models import Service, SocialNetwork, PaymentMethods


class RegisterServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            'category', 'subcategory', 'title', 'company', 'plan', 'cuota',
            'logo', 'image', 'description',
            'address', 'lat', 'lng',
            'email', 'phone1', 'phone2', 'whatsapp', 'web',
            'at_lunes', 'op_lunes', 'cl_lunes',
            'at_martes', 'op_martes', 'cl_martes',
            'at_miercoles', 'op_miercoles', 'cl_miercoles',
            'at_jueves', 'op_jueves', 'cl_jueves',
            'at_viernes', 'op_viernes', 'cl_viernes',
            'at_sabado', 'op_sabado', 'cl_sabado',
            'at_domingo', 'op_domingo', 'cl_domingo',
        ]
        widgets = {
            'category': forms.Select(
                attrs={
                    'class': 'form-control',
                    'data-choices': '{"searchEnabled":true, "allowHTML":true,"itemSelectText":""}',
                }
            ),
            'subcategory': forms.SelectMultiple(
                attrs={
                    'class': 'form-select',
                    'data-choices': '{"silent": true,"removeItems": "true","removeItemButton": "true", "allowHTML":true}',
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
                }
            ),
            'cuota': forms.RadioSelect(
                attrs={
                    'class': 'form-check-input plan',
                    # 'data-choices': '{"searchEnabled":false, "allowHTML":true,"itemSelectText":""}',
                }
            ),
            'logo': forms.FileInput(
                attrs={
                    'class': 'form-control w-0 h-0 p-0',
                    'onchange': 'logoPreview(this)',
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control w-0 h-0 p-0',
                    'onchange': 'portadaPreview(this)',
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
            'address': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Dirección',
                }
            ),
            'lat': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'lng': forms.TextInput(
                attrs={
                    'class': 'form-control',
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
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Seleccione...'
        self.fields['subcategory'].empty_label = ''


class UpdateServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            'category', 'title', 'company', 'plan', 'cuota',
            'logo', 'image', 'description',
            'address', 'email', 'phone1', 'phone2', 'whatsapp', 'web',
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
        }


class SocialServiceForm(forms.ModelForm):
    class Meta:
        model = SocialNetwork
        fields = ('name', 'url',)

        widgets = {
            'name': forms.Select(
                attrs={
                    'class': 'form-select',
                    # 'data-choices': '{"searchEnabled":true, "allowHTML":true,"itemSelectText":""}',
                    'style': 'max-width: fit-content;'
                }
            ),
            'url': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Url'
                }
            ),
        }


SocialServiceFormSet = inlineformset_factory(
    Service,
    SocialNetwork,
    form=SocialServiceForm,
    extra=1,
)


class PaymentMethodsServicesForm(forms.ModelForm):
    class Meta:
        model = PaymentMethods
        fields = ('paymethod',)

        widgets = {
            'paymethod': forms.Select(
                attrs={
                    'class': 'form-select',
                    # 'data-choices': '{"searchEnabled":true, "allowHTML":true,"itemSelectText":""}',
                }
            ),
        }


PaymentMethodsServicesFormSet = inlineformset_factory(
    Service,
    PaymentMethods,
    form=PaymentMethodsServicesForm,
    extra=1,
)
