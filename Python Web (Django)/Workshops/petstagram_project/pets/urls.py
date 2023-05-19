from django.urls import path, include
from .views import edit_pet, delete_pet, add_pet, details_pet

urlpatterns = [
    path('add/', add_pet, name='pet-add'),
    path('<str:username>/pet/<slug:pet_name>/', include([
        path('', details_pet, name='pet-details'),   
        path('edit/', edit_pet, name='pet-edit'),
        path('delete/', delete_pet, name='pet-delete'),
    ])),
    
]
