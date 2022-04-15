from dataclasses import fields
from django import forms
from .models import Category, Post


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        Widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Category Name"})
        }

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'category', 'image', 'contents', 'published', 'tags']
