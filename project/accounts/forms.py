from django import forms
from django.contrib.auth.models import User

class Login_Form(forms.ModelForm):
    username=forms.CharField(label='User Name')
    password=forms.CharField(label='Password',widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','password')