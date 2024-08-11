from django import forms
from .models import Post
from django.forms import ModelForm, TextInput, Textarea
from django.core.exceptions import ValidationError


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'short_description', 'text']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок новости', 'maxlength': 50}),
            'short_description': TextInput(attrs={'class': 'form-control',
                                                  'placeholder': 'Краткое описание новости', 'maxlength': 50}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Содержание новости',
                                    'maxlength': 1000, 'style': 'width: 100%; max-width: 200ch;'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise ValidationError('Заголовок не может быть пустым.')
        if len(title) > 50:
            raise ValidationError('Максимальная длина заголовка - 50 символов.')
        return title

    def clean_short_description(self):
        short_description = self.cleaned_data.get('short_description')
        if not short_description:
            raise ValidationError('Краткое описание не может быть пустым.')
        if len(short_description) > 50:
            raise ValidationError('Максимальная длина краткого описания - 50 символов.')
        return short_description

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if not text:
            raise ValidationError('Содержание новости не может быть пустым.')
        if len(text) > 1000:
            raise ValidationError('Максимальная длина содержания - 1000 символов.')
        return text
