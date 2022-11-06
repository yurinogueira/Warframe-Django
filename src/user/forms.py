import re

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.utils.text import slugify

from user.models import User
from user.validators import validate_cpf


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control login-canvas-inputs m-auto",
                "placeholder": "Insira seu E-mail",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Insira sua senha",
                "class": "form-control login-canvas-inputs mt-3 m-auto",
            }
        )
    )


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

    def save(self, commit=True):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        email = User.objects.normalize_email(email)

        self.instance.email = email
        self.instance.username = slugify(email)
        self.instance.set_password(password)

        return super(UserRegisterForm, self).save(commit)

    def clean_email(self) -> str:
        cleaned_data = self.cleaned_data.get("email", "")

        if not re.fullmatch(self.EMAIL_REGEX, cleaned_data):
            raise forms.ValidationError("E-mail inválido")

        return cleaned_data

    def clean_cpf(self) -> str:
        cleaned_data = self.cleaned_data.get("cpf", "")

        validate_cpf(cleaned_data)

        return cleaned_data
