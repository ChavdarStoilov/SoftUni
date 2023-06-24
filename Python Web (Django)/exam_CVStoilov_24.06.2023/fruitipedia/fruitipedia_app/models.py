from django.db import models

# Create your models here.
class Profile(models.Model):
    MAX_FIRST_NAME_LENGTH = 25
    MAX_LAST_NAME_LENGTH = 35
    MAX_EMAIL_LENGTH = 40
    MAX_PASSWORD_LENGTH = 20
    AGE_DEFAULT = 18
    
    
    first_name = models.CharField(
        null=False,
        blank= False,
        max_length= MAX_FIRST_NAME_LENGTH,
    )
    
    last_name = models.CharField(
        null=False,
        blank= False,
        max_length= MAX_LAST_NAME_LENGTH,
        
    )
    
    email = models.EmailField(
        null=False,
        blank= False,
        max_length= MAX_EMAIL_LENGTH,
    )
    
    password = models.CharField(
        null=False,
        blank= False,
        max_length=MAX_PASSWORD_LENGTH,
    )
    
    image_url = models.URLField(
        null=True,
        blank= True,
    )
    
    age = models.IntegerField(
        null=True,
        blank= True,
        default=AGE_DEFAULT,
    )
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
class Fruit(models.Model):
    MAX_NAME_LENGTH = 30
    
    name = models.CharField(
        null=False,
        blank= False,
        max_length= MAX_NAME_LENGTH
    )
    
    image_url = models.URLField(
        null=False,
        blank= False,
    )
    
    description = models.TextField(
        null=False,
        blank= False,        
    )
    
    nutrition = models.TextField(
        null=True,
        blank= True,
    )
    