from django import forms
from products.models import Product
from checkout.models import Order


class StockForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'quantity_available'
        ]


class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'status'
        ]
