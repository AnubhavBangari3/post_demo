from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm

from .models import Post

class SignUpForm(UserCreationForm):
    first_name=forms.CharField(max_length=120,required=False)
    last_name=forms.CharField(max_length=120,required=False)
    email=forms.EmailField(max_length=200,required=False)

    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2',)
        
class PostForm(ModelForm):
    text=forms.CharField(widget=forms.Textarea(attrs={'rows':5,'cols':100}))
    class Meta:
        model=Post
        fields=('text',)