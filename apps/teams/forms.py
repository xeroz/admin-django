from django import forms
from apps.teams.models import Team

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