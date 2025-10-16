from django import forms
from .models import *

class userdata(forms.ModelForm):
    class Meta:
        model=signup_data
        fields='__all__'