from .models import Order
from django.forms import ModelForm, TextInput, DateInput
from datetime import date
from phone_field import PhoneField


class OrderForm(ModelForm):
    class Meta:
        model = Order
        today = date.today()
        date = today.strftime("%Y/%m/%d")
        tickets = []
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
            'date': date,
            'tickets': tickets
        }
