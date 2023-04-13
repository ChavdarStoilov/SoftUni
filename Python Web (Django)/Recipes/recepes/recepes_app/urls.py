from django.urls import path
from recepes_app.views import *

urlpatterns = [
    path('', home, name="home page"),
    path('create/', create, name="create recepe"),
    path('edit/<int:pk>/', edit_recipe, name="edit recepe"),
    path('delete/<int:pk>/', delete_recipe, name="delete recepe"),
    path('details/<int:pk>/', recipe_details, name="recipe details"),
]
