from django import forms
from django.forms import ModelForm

from .models import *

class AuthorForm(forms.ModelForm):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)

    class Meta:
        model = Author
        fields = '__all__'