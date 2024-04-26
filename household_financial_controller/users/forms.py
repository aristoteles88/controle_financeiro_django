from django import forms
# from .models import User
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=25)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password']
