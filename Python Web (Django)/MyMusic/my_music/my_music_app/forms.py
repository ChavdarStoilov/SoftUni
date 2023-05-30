from django import forms
from .models import Profile, Album
from django.core import validators

class ProfileCreateForm(forms.Form):
    MIN_USERNAME_LENGTH = 2
    MAX_USERNAME_LENGTH = 15
    
    username = forms.CharField(
        validators = validators([
            validators.MinLengthValidator(MIN_USERNAME_LENGTH),
            validators.MaxLengthValidator(MAX_USERNAME_LENGTH),
            
        ])
    )
    
    class Meta:
        model = Profile
        fields = (
            'username', 'email', 'age'
        )