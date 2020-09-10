from django.core.exceptions import ValidationError

def validate_valor_calificacion(value):
    if value < -5 or value > 5:
        raise ValidationError("valor calificacion no valida")
    else:
        return value
