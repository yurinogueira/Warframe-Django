from django import forms

from category.models import Category
from product.models import Product


class EditProductForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())
    stock = forms.IntegerField(widget=forms.TextInput())


class ProductForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm",
            "maxlength": "64",
        }),
        required=True,
    )
    item_type = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Selecione uma categoria",
        widget=forms.Select(attrs={
            "class": "form-control form-control-sm",
        }),
        required=True,
    )
    price = forms.DecimalField(
        localize=True,
        min_value=0,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm",
            "value": "",
            "onkeypress": "return (event.charCode >= 48 && event.charCode <= 57) || event.charCode == 44",
        }),
        required=False,
    )
    stock = forms.IntegerField(
        localize=True,
        min_value=0,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm",
            "value": "",
            "onkeypress": "return event.charCode >= 48 && event.charCode <= 57",
        }),
        required=False,
    )

    class Meta:
        model = Product
        fields = (
            "item_type",
            "name",
            "stock",
            "price",
        )
