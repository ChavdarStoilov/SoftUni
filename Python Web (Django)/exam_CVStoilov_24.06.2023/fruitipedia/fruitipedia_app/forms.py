from django import forms
from .validators import validator_start_with_letter, validator_name_fruits
from django.core import validators
from .models import Profile, Fruit

class CreateProfiletForm(forms.ModelForm):
    MIN_FIRST_NAME_LENGTH = 2
    MIN_LAST_NAME_LENGTH = 1
    MIN_PASSWORD_LENGTH = 8
    
    first_name = forms.CharField(
        widget= forms.TextInput(attrs={'placeholder':"First Name"}),
    
        label="",
        validators=[
            validator_start_with_letter,
            validators.MinLengthValidator(MIN_FIRST_NAME_LENGTH),
        ],
        
        
    )
    
    last_name = forms.CharField(
        widget= forms.TextInput(attrs={'placeholder':"Last Name"}),
        label="",
        validators=[
            validator_start_with_letter,
            validators.MinLengthValidator(MIN_LAST_NAME_LENGTH),

        ],
    )
    
    email = forms.EmailField(
        widget= forms.TextInput(attrs={'placeholder':"Email"}),
        label="",
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':"Password"}),
        label="",
        validators=[
            validators.MinLengthValidator(MIN_LAST_NAME_LENGTH),
        ],
    )
    
    
    class Meta:
        model = Profile
        fields = (
            'first_name', 'last_name', 'email', 'password',
        )



class FruitForm(forms.ModelForm):
    MIN_NAME_LENGTH = 2
    
    name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder':"Fruit Name"}),
        validators=[
            validator_name_fruits,
            validators.MinLengthValidator(MIN_NAME_LENGTH),
        ],
    )
    image_url = forms.URLField(
        label="",
        widget=forms.URLInput(attrs={'placeholder':"Fruit Image URL"})
    )
    description = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={'placeholder':"Fruit Description"})
        
    )
    nutrition =  forms.CharField(
        label="",
        widget=forms.Textarea(attrs={'placeholder':"Nutrition Info"}),
        required=False,
    )
    
    class Meta:
        model = Fruit
        fields = '__all__'
        

class EditFruitForm(forms.ModelForm):
    MIN_NAME_LENGTH = 2
    
    name = forms.CharField(
        label="Name:",
        widget=forms.TextInput(attrs={'placeholder':"Fruit Name"}),
        validators=[
            validator_name_fruits,
            validators.MinLengthValidator(MIN_NAME_LENGTH),
        ],
    )
    image_url = forms.URLField(
        label="Image URL:",
        widget=forms.URLInput(attrs={'placeholder':"Fruit Image URL"})
    )
    description = forms.CharField(
        label="Description:",
        widget=forms.Textarea(attrs={'placeholder':"Fruit Description"})
        
    )
    nutrition =  forms.CharField(
        label="Nutrition:",
        widget=forms.Textarea(attrs={'placeholder':"Nutrition Info"}),
        required=False,
    )
    
    class Meta:
        model = Fruit
        fields = '__all__'
    
    
class DeleteFruitForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.keys():
            if field:
                self.fields[field].disabled = True
                self.fields[field].widget.attrs["readonly"] = True

    class Meta:
        model = Fruit
        fields = '__all__'
    
    
    def save(self, commit=True):
        if commit:
           self.instance.delete()
           

class EditProfileForm(forms.ModelForm):
    MIN_FIRST_NAME_LENGTH = 2
    MIN_LAST_NAME_LENGTH = 1
    
    first_name = forms.CharField(
        label="First Name:",
        validators=[
            validator_start_with_letter,
            validators.MinLengthValidator(MIN_FIRST_NAME_LENGTH),
        ],
        
        
    )
    
    last_name = forms.CharField(
        label="Last Name:",
        validators=[
            validator_start_with_letter,
            validators.MinLengthValidator(MIN_LAST_NAME_LENGTH),

        ],
    )
    
    image_url = forms.URLField(
        label="Image URL:",
        required=False,
    )
    
    age = forms.IntegerField(
        label="Age:",
        required=False,
    )
    
    class Meta:
        model = Profile
        fields = (
            'first_name', 'last_name', 'image_url', 'age',
        )