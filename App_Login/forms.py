from django import forms
from .models import User_Profile


class ProfilePicForm(forms.ModelForm):

    class Meta:
        model = User_Profile
        fields = ("profile_pic",)
