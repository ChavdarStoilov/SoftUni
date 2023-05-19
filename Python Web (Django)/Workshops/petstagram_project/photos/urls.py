from django.urls import path, include
from .views import detail_photo, edit_photo, add_photo

urlpatterns = [
    path('add/', add_photo, name='photo-add'),
    path('<int:pk>/', include([
        path('', detail_photo, name='photo-detail'),
        path('edit/', edit_photo, name='photo-edit'),
        ])),
]
