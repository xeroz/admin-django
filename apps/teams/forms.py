from django import forms
from apps.teams.models import Team, Stadium

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('name', 'foundation',)

        labels = {
            'name' : 'Name',
            'fondation' : 'Foundation',
        }

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'required': False}),
            'foundation' : forms.TextInput(attrs={'class':'form-control'}),
        }

class StadiumForm(forms.ModelForm):
    class Meta:
        model = Stadium
        prefix = 'stadium'
        fields = ('name', 'image', 'capacity',)

        labels = {
            'name': 'Name Stadium',
            'image': 'Image',
            'capacity': 'Capacity',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'capacity': forms.TextInput(attrs={'class':'form-control'}),
            'image' : forms.FileInput(attrs={'class':'form-control filestyle',
                                             'data-classinput':'form-control inline',
                                             'data-classbutton':'btn btn-default'}),
        }