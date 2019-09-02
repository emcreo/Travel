from django.forms import ModelForm, TextInput
from .models import Search

class SearchForm(ModelForm):
    class Meta:
        model = Search
        fields = ['city',]
        labels = {
            'cities' : 'Your City',
        }