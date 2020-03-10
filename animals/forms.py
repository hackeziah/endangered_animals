from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'created_by']

# class ImageUploadForm(forms.Form):
#     my_image = forms.ImageField()


# class AccountAuthenticationForm(forms.ModelForm):
