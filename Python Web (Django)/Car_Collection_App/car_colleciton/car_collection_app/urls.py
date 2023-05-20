from django.urls import path, include
from .views import index, catalogue, create_profile, edit_profile, \
    delete_profile, detail_profile, create_car, detail_car, edit_car, delete_car

urlpatterns = [
    path('', index, name='home page'),
    
    path('catalogue', catalogue, name='catalogue page'),
    
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
        path('detail/', detail_profile, name='detail profile'),
    ])),
    
    path('car/', include([
        path('create/', create_car, name='create car'),
        
        path('<int:pk>/', include([
            path('detail/', detail_car, name='detail car'),
            path('edit/', edit_car, name='edit car'),
            path('delete/', delete_car, name='delete car'),
        ]))
    ]))
]
