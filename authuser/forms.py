from django import forms
from authuser.models import User

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email',max_length=100)
    password = forms.CharField(label='Password',widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['phone_number','email','name','password']
