from django import forms
from .models import Song

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['Tittle', 'Artist', 'Album','Year_of_release','Audio_file']





        labels = {
            'Tittle': '',
            'Artist': '',
            'Album': '',
            'Year_of_release': '',
            'Audio_file': '',
        }
        widgets = {
             'Tittle': forms.TextInput(attrs={'placeholder': ' Tittle'}),
             'Artist': forms.TextInput(attrs={'placeholder': ' Artist'}),
             'Album': forms.TextInput(attrs={'placeholder': ' Album'}),
             'Year_of_release': forms.TextInput(attrs={'placeholder': ' Year_of_release'}),
             'Audio_file': forms.TextInput(attrs={'placeholder': ' Audio_file'})
        }
        
