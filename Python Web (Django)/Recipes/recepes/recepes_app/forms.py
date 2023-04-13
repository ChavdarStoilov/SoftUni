from django import forms
from .models import Recepe


class RecepeForm(forms.ModelForm):
    
    class Meta:
        model = Recepe
        fields = ('__all__')


class DeletedRecepeForm(forms.ModelForm):

    class Meta:
        model = Recepe
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    
    def save(self, commit=True):
        if commit:
            self.instance.delete()

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'