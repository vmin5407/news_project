from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import News
from django.forms import ModelForm, RadioSelect


class RegForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'text', 'photo', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст',
                'style': 'resize: none; height: 100px'
            }),
            'photo': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Добавьте фото'
            }),
            'category': RadioSelect(),
        }