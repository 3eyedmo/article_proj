from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password2(self):
        # between 8 and 25 charachters.
        # password must contain atleast one uppercase
        # password must contain atleast one lowercase
        # password must contain atleast on special characters
        # special charachters: @&^%$# 
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match")
        return password2
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 8:
            raise ValidationError("username must be atleast 8 characters!")
        return username
    
    # def clean_email(self):
    #     ...
    

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
