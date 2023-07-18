from django.contrib.auth.forms import UserCreationForm
from django.contrib. auth import get_user_model
from django import forms

user_model = get_user_model()

class CreationForm(UserCreationForm):
    
    class Meta:
        model = user_model
        fields = (
            'username', 'password1', 'password2',
        )
        

class LoginForm(forms.ModelForm):
    
    class Meta:
        model = user_model
        fields = (
            'username', 'password',
        )