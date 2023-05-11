from django import forms

from .models import NewsModel


class NewsForm(forms.ModelForm):
    class Meta:
        model = NewsModel
        fields = ['text', 'author', 'title_news']
        help_texts = {
            'text': 'text'
        }

