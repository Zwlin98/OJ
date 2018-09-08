from django import forms

from .models import User


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=6)
    email = forms.EmailField()
    password_first = forms.CharField(max_length=20, min_length=6)
    password_second = forms.CharField(max_length=20, min_length=6)


# muban
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(max_length=20, required=True, min_length=6)


class FindForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField(max_length=20, min_length=6)


class ResetForm(forms.Form):
    email = forms.EmailField()
    password_first = forms.CharField(max_length=20, min_length=6)
    password_second = forms.CharField(max_length=20, min_length=6)
