from django.db import models

class Profile(models.Model):
    
    username = models.CharField()
    
    email = models.EmailField()
    
    age = models.IntegerField()
    

class Album(models.Model):
    
    album_name = models.CharField()
    
    artist = models.CharField()
    
    genre = models.CharField()
    
    description = models.CharField()
    
    image_url = models.URLField()
    
    price = models.FloatField()
    