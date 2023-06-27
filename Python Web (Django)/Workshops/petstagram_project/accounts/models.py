from django.db import models

# Create your models here.

class UserProfile(models.Model):
    
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Do not show', 'Do not show'),
    )
    
    MAX_CHOICES_LENGTH = 13
    
    username = models.CharField(
        
    )
    password = models.CharField(
        
    )
    email_address = models.EmailField(
        
    )
    first_name = models.CharField(
        
    )
    last_name = models.CharField(
        
    )
    profile_picture = models.URLField(
        
    )
    gender = models.CharField(
        choices=GENDER_CHOICES,
        max_length=MAX_CHOICES_LENGTH,
    )