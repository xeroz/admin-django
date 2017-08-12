from django import forms
from apps.teams.models import Team, Stadium


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = (
            'name',
            'foundation',
            'image'
        )

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': False
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control filestyle',
                    'data-classinput': 'form-control inline',
                    'data-classbutton': 'btn btn-default'
                }
            ),
            'foundation': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class StadiumForm(forms.ModelForm):
    prefix = 'stadium'

    class Meta:
        model = Stadium
        fields = (
            'name',
            'image',
            'capacity',
        )

        labels = {
            'name': 'Name',
            'image': 'Image',
            'capacity': 'Capacity',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control filestyle',
                    'data-classinput': 'form-control inline',
                    'data-classbutton': 'btn btn-default'
                }
            ),
            'capacity': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
        }
