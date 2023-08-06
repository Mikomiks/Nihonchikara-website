from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from django.core.mail import send_mail


class CreateUserForm(UserCreationForm):
    required_css_class = 'This Field is Required!'
    username = forms.EmailField(widget=forms.TextInput(attrs={"class": "form-filds-py", "placeholder": "Input Your Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-filds-py", "placeholder": "Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-filds-py", "placeholder": "ConfirmPassword"}))
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


