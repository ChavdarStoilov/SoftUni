from django.db import models

class Profiel(models.Model):
    USERNAME_MAX_LENGTH = 10
    PASSWORD_MAX_LENGTH = 30
    NAMES_NAME_MAX_LENGTH = 30
    username= models.CharField(
        null=False,
        blank=False,
        max_length=USERNAME_MAX_LENGTH,
        
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.IntegerField(
        null=False,
        blank=False,
    )
    password = models.CharField(
        null=False,
        blank=False,
        max_length=PASSWORD_MAX_LENGTH,
    )
    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=NAMES_NAME_MAX_LENGTH,
    )
    last_name = models.CharField(
        null=True,
        blank= True,
        max_length=NAMES_NAME_MAX_LENGTH,
    )
    profile_pricutre = models.URLField(
        null=True,
        blank= True,
    )

    
    def name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name and not self.last_name:
            return f'{self.first_name}'
        elif self.last_name and not self.first_name:
            return f'{self.last_name}'
        else:
            return False
        
class Car(models.Model):
    TYPE_MAX_LENGTH = 10
    MODEL_MAX_LENGTH = 20
    TYPE_CARS = (
        ('Sprot Car', 'Sport Car'),
        ('Pickup', 'Pickup'),
        ('Crossover', 'Crossover'),
        ('Minibus', 'Minibus'),
        ('Other', 'Other')
    )
    type = models.CharField(
        null=False,
        blank=False,
        max_length=TYPE_MAX_LENGTH,
        choices=TYPE_CARS,
    )
    model = models.CharField(
        null=False,
        blank=False,
        max_length=MODEL_MAX_LENGTH
    )
    year = models.IntegerField(
        null=False,
        blank=False,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        
    )
    price = models.FloatField(
        null=False,
        blank=False,
        
    )