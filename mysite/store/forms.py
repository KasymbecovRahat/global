from django import forms
from .models import Product

class ProductFilter(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'category', 'have', 'price', 'description', 'image',]
