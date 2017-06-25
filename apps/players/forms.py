from django import forms
from apps.players.models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = (
            'name',
            'lastname',
            'number',
            'position',
            'team',)

        labels = {
            'name' : 'Name',
            'lastname' : 'Lastname',
            'number' : 'Number',
            'position' : 'Position',
            'team' : 'Team',
        }

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'required': False}),
            'lastname' : forms.TextInput(attrs={'class':'form-control'}),
            'number' : forms.TextInput(attrs={'class':'form-control'}),
            'position' : forms.TextInput(attrs={'class':'form-control'}),
            'team' : forms.Select(attrs={'class':'form-control'}),
        }