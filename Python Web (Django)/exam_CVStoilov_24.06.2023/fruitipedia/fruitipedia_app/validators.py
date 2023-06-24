from django.core.exceptions import ValidationError

# def validator_min_length(value):
#     if value < 2:
#         raise ValidationError(("%(value)s is not an even number"),
#             params={"value": value},
#         )

def validator_start_with_letter(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")

def validator_min_length_passwords(value):
    pass

def validator_min_age(value):
    pass


def validator_name_fruits(value):
    
    if not value.isalpha():
        raise ValidationError("Fruit name should contain only letters!")