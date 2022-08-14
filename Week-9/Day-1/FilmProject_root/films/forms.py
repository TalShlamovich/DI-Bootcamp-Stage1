from django import forms
from .models import Country, Film, Director

class AddFilmForm(forms.ModelForm):
    
    class Meta:
        model = Film
        fields = '__all__'

class AddDirectorForm(forms.ModelForm):

    class Meta:
        model = Director
        fields = '__all__'

class AddCountryForm(forms.ModelForm):

    class Meta:
        model = Country
        fields = '__all__'