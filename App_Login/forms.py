from django import forms
from .models import User_Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class ProfilePicForm(forms.ModelForm):

    class Meta:
        model = User_Profile
        fields = ("profile_pic",)

class UserChangeForms(UserChangeForm):
    class Meta:
        model = User
        fields = ("username",'first_name','last_name','email')
        exclude = ['password',]