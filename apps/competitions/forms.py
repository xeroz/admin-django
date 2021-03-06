from django import forms
from apps.competitions.models import Competition


class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = (
            'name',
            'image',
            'team',)

        labels = {
            'name': 'Name',
            'image': 'Image',
            'team': 'Teams',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'team': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'id': 'select2-3'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control filestyle',
                    'data-classinput': 'form-control inline',
                    'data-classbutton': 'btn btn-default'
                }
            ),
        }
