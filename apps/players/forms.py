from django import forms
from apps.players.models import Player, Statistics
from django_countries.widgets import CountrySelectWidget

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = (
            'name',
            'lastname',
            'number',
            'position',
            'team',
            'image',
            'country',)

        labels = {
            'name' : 'Name',
            'lastname' : 'Lastname',
            'number' : 'Number',
            'position' : 'Position',
            'team' : 'Team',
            'image': 'Image',
            'country': 'Country',
        }

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'required': False}),
            'lastname' : forms.TextInput(attrs={'class':'form-control'}),
            'number' : forms.TextInput(attrs={'class':'form-control'}),
            'position' : forms.TextInput(attrs={'class':'form-control'}),
            'team' : forms.Select(attrs={'class':'form-control'}),
            'country' : CountrySelectWidget(attrs={'class':'form-control', 'id': 'select2-1'}),
            'image' : forms.FileInput(attrs={'class':'form-control filestyle',
                                             'data-classinput':'form-control inline',
                                             'data-classbutton':'btn btn-default'}),
        }

class StatisticForm(forms.ModelForm):
    class Meta:
        model = Statistics
        fields = (
            'pace',
            'shooting',
            'passing',
            'dribbling',
            'defending',
            'physical',
        )

        widgets = {
            'pace': forms.TextInput(attrs={'class':'form-control'}),
            'shooting': forms.TextInput(attrs={'class':'form-control'}),
            'passing': forms.TextInput(attrs={'class':'form-control'}),
            'dribbling': forms.TextInput(attrs={'class':'form-control'}),
            'defending': forms.TextInput(attrs={'class':'form-control'}),
            'physical': forms.TextInput(attrs={'class':'form-control'}),
}