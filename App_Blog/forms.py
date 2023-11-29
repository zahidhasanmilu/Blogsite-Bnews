from django import forms
from .models import Comment, Blog, Likes


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ("comment",)
