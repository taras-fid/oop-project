from .models import Order
from django.forms import ModelForm, TextInput, DateInput
from datetime import date
from phone_field import PhoneField
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField


class OrderForm(ModelForm):
    class Meta:
        model = Order
        # today = date.today()
        # date = today.strftime("%Y-%m-%d")
        fields = ['name', 'phone', 'mail']
        # Order.date = date
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
            # 'cc_number': TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Номер картки'
            # }),
            # 'cc_expiry': TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Дата сроку картки'
            # }),
            # 'cc_code': TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'CVC код'
            # }),
        }
