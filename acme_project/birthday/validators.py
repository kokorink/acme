from django.core.exceptions import ValidationError
from datetime import date


def real_age(value: date) -> None:
    age = (date.today() - value).days / 365
    if 1 > age or age > 120:
        raise ValidationError(
            'Ожидается возраст от 1 года до 120 лет')
