from django import forms
from .models import Profile, Note


class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ('__all__')


class CreateNote(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('__all__')


class NoteFormn(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('__all__')


class DeteleNote(forms.ModelForm):

    class Meta:
        model = Note
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
