from django.contrib.auth.models import User
from django import forms


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username",)
        labels = {
            "username": "Change your username"
        }