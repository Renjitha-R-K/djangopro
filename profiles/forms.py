
from django import forms
from .models import JobSeekerProfile,EmployerProfile

class JobSeekerProfileForm(forms.ModelForm):
    class Meta:
        model=JobSeekerProfile
        exclude = ["user"]



class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model=EmployerProfile
        exclude = ["user"]