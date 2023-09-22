from django.db import models

# Create your models here.

class Ingredient(models.Model):

    primary_color = models.CharField(max_length=7, default="#FFFFFF")
