from django.core.exceptions import ValidationError


def intiger_validate(value):
    if value:
        for char in value:
            if not char.isdigit():
                raise ValidationError("To pole może zawierać tylko cyfry.")
