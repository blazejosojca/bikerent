from django.core.exceptions import ValidationError


def validate_password(value):
    if value < 3:
        raise ValidationError("{} haslo jest za krótkie".format(value))
