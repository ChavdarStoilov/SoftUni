from django.core.exceptions import ValidationError
import re

def username_validator(username):
    if "_" in username:
        if username.isalnum():
            pass
    else:
        raise ValidationError(
            ("Ensure this value contains only letters, numbers, and underscore."),
        )