from django import forms
from .models import Project,Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['profile_picture','bio','email','phone_number'] 

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields=['title','image','description','country','link']         
 