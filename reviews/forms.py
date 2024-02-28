from django import forms
from .models import ReviewPost


class CreatePost(forms.ModelForm):
    class Meta:
        model = ReviewPost
        exclude = ('slug', 'author', 'status',)


class EditPost(forms.ModelForm):
    """
    This is the Form to update the Users account
    """
    class Meta:
        model = ReviewPost
        exclude = ('slug', 'author', 'status',)
