from .models import Order
from django.forms import ModelForm, TextInput


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'mail', 'tickets']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Им`я покупця'
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефону'
            }),
            'mail': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Поштова адреса'
            }),
            'tickets': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Білети'
            }),
        }