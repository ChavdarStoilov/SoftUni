from django.urls import path
from .views import IndexView, LoginView, RegisterView

urlpatterns = [
    path("", IndexView.as_view(), name='home page'),
    # path("login/", LoginView.as_view(), name='login page'),
    # path('register/', RegisterView.as_view(), name='register page'),
]
