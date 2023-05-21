from django.urls import path, include
from .views import index, dashboard, create_profile, details_profile, \
    edit_profile, delete_profile, create_game, details_game, edit_game, delete_game

urlpatterns = [
    path('', index, name="home page"),
    
    path('dashboard/', dashboard, name="dashboard page"),

    path('profile/', include([
        path('create/', create_profile, name="create profile page"),
        path('details/', details_profile, name="details profile page"),
        path('edit/', edit_profile, name="edit profile page"),
        path('delete/', delete_profile, name="delete profile page"),
    ])),

    path('game/', include([
        path('create/', create_game, name="create game page"),
        path('details/<int:pk>/', details_game, name="details game page"),
        path('edit/<int:pk>/', edit_game, name="edit game page"),
        path('delete/<int:pk>', delete_game, name="delete game page"),
    ]))

]
