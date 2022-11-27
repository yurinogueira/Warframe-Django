from django import forms

from category.models import Category
from core.models import Image
from market.models import SellItem


class SearchSellItemForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm",
            "maxlength": "64",
        }),
        required=False,
    )


class SellItemForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm",
            "maxlength": "64",
        }),
        required=True,
    )
    description = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm",
            "maxlength": "256",
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
    image = forms.ModelChoiceField(
        queryset=Image.objects.all(),
        empty_label="Selecione uma imagem",
        widget=forms.Select(attrs={
            "class": "form-control form-control-sm",
        }),
        required=True,
    )
    created_at = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            "class": "form-control form-control-sm",
        }),
        required=False,
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
    is_available = forms.BooleanField(
        widget=forms.CheckboxInput(),
        required=False,
    )

    class Meta:
        model = SellItem
        fields = (
            "item_type",
            "name",
            "description",
            "stock",
            "image",
            "price",
            "is_available",
            "created_at",
        )
