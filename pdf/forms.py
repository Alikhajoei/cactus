from django import forms
from .models import Genre, Book, NewsEmail


class signupForm(forms.Form):
    name = forms.CharField(label='name', max_length=20)
    username = forms.CharField(label='username', max_length=20)
    password = forms.CharField(label='password', max_length=20)


class fileAttach(forms.ModelForm):
    class Meta:
        model=Book
        exclude=("user",)

