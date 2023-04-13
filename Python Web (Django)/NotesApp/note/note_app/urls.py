from django.urls import path
from .views import index, add_note, edit_note, delete_note, details_note, show_prfile
urlpatterns = [
    path("", index, name="home page"),

    path("add/", add_note, name="add note"),
    path("edit/<int:pk>/", edit_note, name="edit note"),
    path("delete/<int:pk>/", delete_note, name="delete note"),
    path("details/<int:pk>/", details_note, name="details"),
    path("profile/", show_prfile, name="profile"),

]
