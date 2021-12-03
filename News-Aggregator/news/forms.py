from django import forms
from . import models

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = models.User
        fields = ('email', 'password')
