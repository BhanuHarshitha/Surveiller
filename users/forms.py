from .models import Profile
from django.contrib.auth.models import User
from django import forms

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


