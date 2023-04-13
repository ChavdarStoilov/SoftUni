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