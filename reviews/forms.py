from django import forms
from django import forms
from .models import Review, Comment
from django.forms import ModelForm, TextInput, Textarea

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content', 'movie_name', 'grade', )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', ]