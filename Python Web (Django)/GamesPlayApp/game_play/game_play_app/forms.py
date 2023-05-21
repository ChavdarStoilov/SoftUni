from django.core import validators
from django import forms
from .models import Profile, Game

class CreateProfileForm(forms.ModelForm):
    MIN_AGE = 12
    MAX_PASSWORD_LENGTH = 30
    
    email = forms.CharField(
        required=True,
    )
    
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput,
        validators=[
            validators.MaxLengthValidator(MAX_PASSWORD_LENGTH)
        ]
    )
    age = forms.IntegerField(
        required=True,
        validators=[
            validators.MinValueValidator(MIN_AGE)
        ]
    )
    
    class Meta:
        model = Profile
        fields = (
            "email", "age", "password",
        )
        
        
        
        
class CreateGameForm(forms.ModelForm, ):
    MAX_TITLE_LENGTH = 30
    CATEGORY_MAX_LENGTH = 15
    MIN_RATING = 0.1
    MAX_RATING = 5.0
    MIN_LEVEL = 1
    
    title = forms.CharField(
        required=True,
        validators=[
            validators.MaxLengthValidator(MAX_TITLE_LENGTH),
        ]
    )
    
    category = forms.ChoiceField(
        required=True,
        validators=[
            validators.MaxLengthValidator(CATEGORY_MAX_LENGTH),
        ],
        choices=Game.TYPE_CATEGORY,
    )
    
    rating = forms.FloatField(
        required=True,
        validators=[
            validators.MinValueValidator(MIN_RATING),
            validators.MaxValueValidator(MAX_RATING)
        ]
    )
    
    max_level = forms.IntegerField(
        required=False,
        validators=[
            validators.MinValueValidator(MIN_LEVEL)
        ]
    )
    
    image_url = forms.URLField(
        required=True,
    )
    
    summary = forms.Textarea()
    
    class Meta:
        model = Game
        fields = (
            "title", "category", "rating", "max_level", "image_url", "summary",
        )
        
        


class GameDeleteForm(forms.ModelForm):
    
    class Meta:
        model = Game
        fields = (
            "__all__"
        )
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.keys():
            if field:
                self.fields[field].disabled = True
                self.fields[field].widget.attrs["readonly"] = True
                
    def save(self, commit=True):
         if commit:
            self.instance.delete()
            
            

class ProfleForm(CreateProfileForm, forms.ModelForm):
    
    MAX_NAMES_LENGTH = 30
    
    first_name = forms.CharField(
        required=False,
        validators=[
            validators.MaxLengthValidator(MAX_NAMES_LENGTH)
        ]
    )
    
    last_name = forms.CharField(
        required=False,
        validators=[
            validators.MaxLengthValidator(MAX_NAMES_LENGTH)
        ]
    )
    
    class Meta:
        model = Profile
        fields = (
            '__all__'
        )
        
        