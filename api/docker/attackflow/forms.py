from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput)