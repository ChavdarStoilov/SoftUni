from django import forms
from .models import Recepe


class RecepeForm(forms.ModelForm):
    
    class Meta:
        model = Recepe
        fields = ('__all__')

