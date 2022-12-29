from django import forms
from .models import *

class AddMovieForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'
    class Meta:
        model = Movie
        fields = ['name', 'slug', 'content', 'photo', 'is_published', 'category']