from django import forms
from django.core.exceptions import ValidationError

from .models import Advertisement

class AdvertisementForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class']='form-control form-control-lg'
        self.fields['description'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['image'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['price'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['auktion'].widget.attrs['class'] = 'form-check-input'

def clean_title(self):
    title = self.cleaned_data['title']
    if title.startswith('?'):
        raise forms.ValidationError('Заголовок не может начинаться с вопросительного знака')
    return title