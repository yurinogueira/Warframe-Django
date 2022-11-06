import re

from django.core.exceptions import ValidationError

INVALIDS = (
    "11111111111",
    "22222222222",
    "33333333333",
    "44444444444",
    "55555555555",
    "66666666666",
    "77777777777",
    "88888888888",
    "99999999999",
    "00000000000",
)


def __digit_generator(cpf: str, weight: int):
    sum_digit = 0
    for i in range(weight - 1):
        sum_digit = sum_digit + int(cpf[i]) * weight
        weight = weight - 1

    digit = 11 - sum_digit % 11
    return 0 if digit > 9 else digit


def validate_cpf(value: str):
    cpf = re.sub("[^0-9]", "", value)

    if len(cpf) != 11:
        raise ValidationError("O CPF deve conter 11 números")

    first_digit = __digit_generator(cpf, 10)
    second_digit = __digit_generator(cpf, 11)

    if cpf in INVALIDS:
        raise ValidationError("CPF banido")

    if not cpf[-2:] == f"{first_digit}{second_digit}":
        raise ValidationError("Esse CPF não existe")
