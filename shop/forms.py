from django import forms
from .models import *
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'location', 'phone_number']


class UserForm(forms.ModelForm):
    email = forms.EmailField(max_length=300, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')