from django import forms
from .models import Car, Profiel
from .validations import age_validator, username_validator, \
    car_model_validator, price_validator, year_validator

class CreateProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    
    class Meta:
        model = Profiel
        fields = (
            'username', 'email', 'age', 'password',
        )

    
    def clean(self):
        super(CreateProfileForm, self).clean()
        username = self.cleaned_data.get('username')
        age = self.cleaned_data.get('age')
        username_validator(username)
        age_validator(age)
        
    

class CreateCarForm(forms.ModelForm):
    
    class Meta:
        model = Car
        fields = (
            "type", 
            "model", 
            "year", 
            "image_url", 
            "price", 

        )
        
    
    
    def clean(self):
        super(CreateCarForm, self).clean()
        model = self.cleaned_data.get('model')
        year = self.cleaned_data.get('year')
        price = self.cleaned_data.get('price')
        
        car_model_validator(model)
        year_validator(year)
        price_validator(price)
        

class CarForm(forms.ModelForm):
    
    class Meta:
        model = Car
        fields =  fields = (
            "type", 
            "model", 
            "year", 
            "image_url", 
            "price", 

        )
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields.keys():
            if i:
                self.fields[i].disabled = True
                self.fields[i].widget.attrs["readonly"] = True
                
    def save(self, commit=True):
         if commit:
            self.instance.delete()
            
            
            
            
class UserForm(forms.ModelForm):
    
    class Meta:
        model = Profiel
        fields = (
            '__all__'
        )

    
    def clean(self):
        super(UserForm, self).clean()
        username = self.cleaned_data.get('username')
        age = self.cleaned_data.get('age')
        username_validator(username)
        age_validator(age)
        
        
        
class UserDeleteForm(forms.ModelForm):
    
    class Meta:
        model = Profiel
        fields = (
            '__all__'
        )
        
    def save(self, commit=True):
        if commit:
            self.instance.delete()
            