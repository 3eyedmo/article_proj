from typing import Any
from django import forms
from .models import Article
from django.core.exceptions import ValidationError


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['introduction', 'body', 'title']

    def save(self, commit: bool = ...) -> Any:
        return super().save(commit)
    
    def clean_body(self):
        data = self.cleaned_data["body"]
        if int(data):
            raise ValidationError(message="Invalid Body")
        return data
    