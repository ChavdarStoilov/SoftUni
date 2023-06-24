from django.urls import path, include
from .views import index, dashboard, create_fruit, details_fruit, edit_fruit,\
    delete_fruit, create_profile, details_profile , edit_profile, delete_profile


urlpatterns = [
    path("", index, name="home page"),
    path("dashboard/", dashboard, name="dashboard page"),
    path("create/", create_fruit, name="create fruit page"),
    
    path("<int:pk>/", include([
        path("details/", details_fruit, name = "details fruit page"),
        path("edit/", edit_fruit, name = "edit fruit page"),
        path("delete/", delete_fruit, name = "delete fruit page"),
    ])),
    
    path("profile/", include([
        path("create/", create_profile, name= "create profile page"),
        path("details/", details_profile, name= "details profile page"),
        path("edit/", edit_profile, name= "edit profile page"),
        path("delete/", delete_profile, name= "delete profile page"),
        
    ])),
]
