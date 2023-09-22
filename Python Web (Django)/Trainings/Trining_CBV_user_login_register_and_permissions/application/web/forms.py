from django.contrib.auth.forms import UserCreationForm
from django.contrib. auth import get_user_model
from django import forms
from django.forms import ModelForm
from django.forms.widgets import TextInput
from .models import Ingredient
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
        
        



class MyModelForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(MyModelForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields["primary_color"].widget = TextInput(
                attrs={"type": "color", "title": self.instance.primary_color}
            )
            
    class Meta:
        model = Ingredient
        fields = "__all__"
        widgets = {
            "primary_color": TextInput(attrs={"type": "color"}),
        }