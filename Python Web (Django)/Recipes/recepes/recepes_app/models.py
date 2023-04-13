from django.db import models



class Recepe(models.Model):
    title = models.CharField(max_length=30)
    image_url = models.URLField()
    description = models.TextField()
    ingredients = models.CharField(max_length=250)
    time = models.IntegerField()
