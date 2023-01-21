from django import forms
from movieapp1.models import movies

class movieform(forms.ModelForm):
    class Meta:
        model=movies
        fields='__all__'