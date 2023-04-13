from django.db import models

# Create your models here.

class Profile(models.Model):
    FIRST_NAME_AND_LAST_NAME_MAX_LENGTH = 20


    first_nam  = models.CharField(max_length = FIRST_NAME_AND_LAST_NAME_MAX_LENGTH)
    last_name = models.CharField(max_length = FIRST_NAME_AND_LAST_NAME_MAX_LENGTH)
    age = models.IntegerField()
    image_url = models.URLField()


class Note(models.Model):
    NOTE_TITLE_MAX_LENGTH = 50

    title  = models.CharField(max_length = NOTE_TITLE_MAX_LENGTH)
    image_url =  models.URLField()
    content  = models.TextField()