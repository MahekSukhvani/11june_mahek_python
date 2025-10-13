from django import forms
from .models import *
from django.core.exceptions import ValidationError


class userform(forms.ModelForm):
    class Meta:
        model=userrdata
        fields='__all__'
        widgets = {
            'password': forms.PasswordInput(),
            'cpassword': forms.PasswordInput(),   
       }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        cpassword = cleaned_data.get("cpassword")

        # Raise field-specific error
        if password and cpassword and password != cpassword:
            self.add_error('cpassword', "Passwords do not match")  
        return cleaned_data
       