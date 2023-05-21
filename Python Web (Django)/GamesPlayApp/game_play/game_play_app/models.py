from django.db import models

class Profile(models.Model):
    
    
    email = models.EmailField()
    
    age = models.IntegerField()
    
    password = models.CharField()

    
    first_name = models.CharField(
        null=True,
        blank=True,
    )
    
    last_name = models.CharField(
        null=True,
        blank=True,
    )
    
    
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    
    def get_name(self):
        if self.first_name and not self.last_name:
            return self.first_name
        elif self.last_name and not self.first_name:
            return self.last_name
        elif self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        
class Game(models.Model):
    
    TYPE_CATEGORY = [
        ("Action", "Action"),
        ("Adventure", "Adventure"),
        ("Puzzle", "Puzzle"),
        ("Strategy", "Strategy"),
        ("Sports", "Sports"),
        ("Board/Card Game", "Board/Card Game"),
        ("Other", "Other"),
    ]
    
    
    
    title = models.CharField(
        unique=True,
    )

    category = models.CharField(
        choices=TYPE_CATEGORY,
    )


    rating = models.FloatField()

    max_level = models.IntegerField()

    image_url = models.URLField()

    summary = models.TextField()

