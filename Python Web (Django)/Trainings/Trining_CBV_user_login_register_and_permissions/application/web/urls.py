from django.urls import path
from .views import IndexView, login_view, RegisterView, testView

urlpatterns = [
    path("", IndexView.as_view(), name='home page'),
    path("login/", login_view, name='login page'),
    path('register/', RegisterView.as_view(), name='register page'),
    path('test/', testView.as_view(), name='test')
]
