from django import forms
from .models import *

class RegisterForm(forms.ModelForm):
    class Meta :
        model = RegisterModel
        fields = "__all__"

class LoginForm(forms.Form):
    email = forms.EmailField(required=False, label="Email Id")
    password = forms.CharField(max_length=100, required=False)
    