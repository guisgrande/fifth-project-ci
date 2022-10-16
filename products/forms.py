from django import forms
from .models import Product, Category, Offer


class ProductForm(forms.ModelForm):
    """
    Form class to admin add product.
    """

    class Meta:
        model = Product
        fields = [
            'name',
            'category',
            'description',
            'price',
            'rating',
            'product_image',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
