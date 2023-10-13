from django import forms
from .models import Destination, Cruise, InfoRequest


class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'description']
        labels = {
            'name': 'Destination Name',
            'description': 'Destination Description',
        }
        help_texts = {
            'name': 'Enter the name of the destination',
            'description': 'Enter a description of the destination',
        }
        error_messages = {
            'name': {
                'max_length': 'This destination name is too long.',
            },
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }


