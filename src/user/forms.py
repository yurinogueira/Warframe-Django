import re

from django import forms

from user.models import User
from user.validators import validate_cpf


class UserRegisterForm(forms.ModelForm):
    EMAIL_REGEX = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")

    email = forms.CharField(
        error_messages={
            "required": "Campo obrigatório",
            "unique": "E-mail já cadastrado",
        },
        widget=forms.widgets.EmailInput(
            attrs={
                "placeholder": "Endereço de E-mail",
                "class": "form-control login-canvas-inputs m-auto",
            }
        ),
        label="",
    )
    first_name = forms.CharField(
        error_messages={"required": "Campo obrigatório"},
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Nome",
                "class": "form-control login-canvas-inputs m-auto",
            }
        ),
        label="",
    )
    last_name = forms.CharField(
        error_messages={"required": "Campo obrigatório"},
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Sobrenome",
                "class": "form-control login-canvas-inputs m-auto",
            }
        ),
        label="",
    )
    cpf = forms.CharField(
        error_messages={"required": "Campo obrigatório"},
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "CPF",
                "class": "form-control login-canvas-inputs m-auto",
            }
        ),
        label="",
    )
    password = forms.CharField(
        error_messages={"required": "Campo obrigatório"},
        widget=forms.widgets.PasswordInput(
            attrs={
                "placeholder": "Senha",
                "class": "form-control login-canvas-inputs m-auto",
            }
        ),
        label="",
    )

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "cpf",
            "password",
        )

    def clean_email(self) -> str:
        cleaned_data = self.cleaned_data.get("email", "")

        if not re.fullmatch(self.EMAIL_REGEX, cleaned_data):
            raise forms.ValidationError("E-mail inválido")

        return cleaned_data

    def clean_cpf(self) -> str:
        cleaned_data = self.cleaned_data.get("cpf", "")

        validate_cpf(cleaned_data)

        return cleaned_data
