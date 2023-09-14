from django import forms

class signUpForm(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64)
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)

class logInForm(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64)
