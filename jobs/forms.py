from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model=Job
        exclude=['employer']
        widgets = {
            'deadline': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }