from django.db import models

# Create your models here.
class PetPhoto(models.Model):
    DESC_MAX_LENGTH = 300
    MAX_LOCATION_LENGTH = 30
    
    photo = models.ImageField(
        
    )
    
    description = models.TextField(
        max_length=DESC_MAX_LENGTH,
    )
    
    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
    )
    
    # tagged_pets = 