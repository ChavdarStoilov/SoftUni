
from django.core.exceptions import ValidationError

def username_validator(username):
    if len(username) < 2:
        raise ValidationError(
            'The username must be a minimum of 2 chars'
        )
    
    
def age_validator(age):
    if int(age) < 18:
        raise ValidationError(
            ('The age cannot be below %(value)s'),
            params={"value": "18"},
        )
    
    
    
def car_model_validator(model):
    if len(model) < 2:
        raise ValidationError(
            'The model must be a minimum of 2 chars'
            # ('The model must be a minimum of %(value)s chars'),
            # params={"value": "2"},
        )
    
    
def year_validator(years):
    if 2049 < int(years) or int(years) < 1980 :
         raise ValidationError(
            ('Year must be between %(min_year)s and %(max_year)s'),
            params={
                "min_year": "1980",
                "max_year": "2049"
                },
        )
         
         
def price_validator(price):
    if int(price) < 1:
        raise ValidationError(
            ('The price cannot be below %(value)s'),
            params={
                "value": "1",
                },
        )
         