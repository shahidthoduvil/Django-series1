from .models import *
from django.forms import ModelForm


class PostForm(ModelForm):
    class Meta:
        model=Post
        fields='__all__'
