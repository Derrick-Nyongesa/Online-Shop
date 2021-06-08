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


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['title', 'feedback']


class SubscriptionForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    email = forms.EmailField(label='Email')


class PaymentForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    email = forms.EmailField(label='Email')
    address = forms.CharField(label='Address', max_length=100)
    card_number = forms.IntegerField(label='Card Number')

