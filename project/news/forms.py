from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'title','type','text'}

    def clean(self):
        cleaned_data=super().clean()
        title=cleaned_data.get('title')


        if title[0].islower():
            raise ValidationError({
                'title':'the title should start with uppercase letter'
            })
        return cleaned_data
