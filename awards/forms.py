from django import forms
from .models import Project,Profile,Review, RATE_CHOICES

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['profile_picture','bio','email','phone_number'] 
