from django import forms
from .models import Post, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description", "category", "image", "is_active", "tags"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Заголовок поста"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "Текст поста"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "tags": forms.SelectMultiple(attrs={"class": "form-control"}),
        }
        labels = {
            "title": "Заголовок",
            "description": "Описание",
            "category": "Категория",
            "image": "Изображение",
            "is_active": "Опубликовано",
            "tags": "Теги",
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Название категории"}),
        }
        labels = {
            "name": "Название категории",
        }