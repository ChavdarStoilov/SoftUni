from django.db import models

# Create your models here.
class Pet(models.Model):
    name =  models.CharField(
        
    )
    personal_pet_photo = models.URLField(
        
    )
    date_of_birth = models.DateField(
        
    )
    slug  = models.CharField(
        
    )
    
