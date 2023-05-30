from django.urls import path, include
from .views import index, profile_datails, profile_delete,\
    album_add, album_details, album_edit, album_delete

urlpatterns = [
    path('', index, name='home page'),
    
    path('profile/', include([
        path('details/', profile_datails, name='profile details page'),
        path('delete/', profile_delete, name='profile delete page'),
        
    ])),
    
    path('album/', include([
        path('add/', album_add, name='album add page'),
        path('details/', album_details, name='album details page'),
        path('edit/', album_edit, name='album edit page'),
        path('delete/', album_delete, name='album delete page'),
        
    ]))
]
