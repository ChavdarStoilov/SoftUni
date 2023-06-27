# from django.core.exceptions import ValidationError
import re

# def username_validator(username):
#     if not "_" in username:
#         raise ValidationError(
#             ("Ensure this value contains only letters, numbers, and underscore."),
#         )

        
        
user = "adad123_"
result = re.search("\W", user)
(result)