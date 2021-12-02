from django import forms
from . import models

NEWS_CHOICES = (('1', 'Times of India'),
                ('2', 'Hindustan Times'),
                ('3', 'India Today'),
                ('4','NDTV'))

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    news_media = forms.MultipleChoiceField(widget=forms.CheckboxInput(),
                      choices=NEWS_CHOICES)
    class Meta:
        model = models.User
        fields = ('username', 'email', 'password', 'favourite_paper')


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = models.User
        fields = ('email', 'password')
