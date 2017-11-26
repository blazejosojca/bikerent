from django.core.exceptions	import ValidationError

def validate_producer_name(value):
    if len(value) < 3:
        raise ValidationError("This word is too short!")
