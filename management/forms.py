from django import forms
from products.models import Product


class StockForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'quantity_available'
        ]
