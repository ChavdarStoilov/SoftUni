from django.contrib import admin
from .models import Note, Profile

# Register your models here.

admin.site.register(Profile)
admin.site.register(Note)