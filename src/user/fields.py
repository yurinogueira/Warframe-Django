from django.db import models

from user.validators import validate_cpf


class CPFField(models.CharField):
    default_validators = [validate_cpf]

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("max_length", 14)
        super().__init__(*args, **kwargs)
