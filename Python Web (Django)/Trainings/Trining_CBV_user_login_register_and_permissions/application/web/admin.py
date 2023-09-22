from django.contrib import admin
from .models import Ingredient
# Register your models here.
from .forms import MyModelForm


@admin.register(Ingredient)
class MyModel(admin.ModelAdmin):
    form = MyModelForm