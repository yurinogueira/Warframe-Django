from django import forms


class SearchSellItemForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm",
            "maxlength": "64",
        }),
        required=False
    )
