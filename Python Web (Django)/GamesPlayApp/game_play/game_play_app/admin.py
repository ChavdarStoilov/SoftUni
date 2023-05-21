from django.contrib import admin
from .models import Game, Profile

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass