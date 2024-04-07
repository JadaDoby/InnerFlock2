""" from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Import User model
from django.contrib.auth.models import User
from .models import UserProfile """

""" class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2'] """

""" class UserForm(forms.Form):
    name = forms.CharField(max_length=255, label='User Name') """

""" class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'school_name'] """ 