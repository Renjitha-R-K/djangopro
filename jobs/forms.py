from django import forms
from .models import Job,Application


class JobForm(forms.ModelForm):
    class Meta:
        model=Job
        exclude=['employer']
        widgets = {
            'deadline': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }


class ApplicationForm(forms.ModelForm):
    class Meta:
        model=Application
        fields=['resume','cover_letter']



class ApplicationUpdateForm(forms.ModelForm):
    class Meta:
        model = Application
        fields=['status','employer_note']