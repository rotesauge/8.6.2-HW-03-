from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = ['caption', 'text']

   def clean(self):
       cleaned_data = super().clean()
       caption = cleaned_data.get("caption")
       text = cleaned_data.get("text")
       if caption == text:
           raise ValidationError("Заголовок не должен быть идентичен тексту новости.")
       return cleaned_data




class ArticleForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = ['caption', 'text']

   def clean(self):
       cleaned_data = super().clean()
       caption = cleaned_data.get("caption")
       text = cleaned_data.get("text")
       if caption == text:
           raise ValidationError("Заголовок не должен быть идентичен тексту статьи.")
       return cleaned_data

 