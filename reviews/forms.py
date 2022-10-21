from cProfile import label
from django import forms
from django import forms
from .models import Review, Comment
from django.forms import ModelForm, TextInput, Textarea

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content', 'movie_name', 'grade', 'image', )
        labels = {
            'title' : '제목',
            'content' : '내용',
            'movie_name' : '영화 제목',
            'grade' : '별점',
            'image' : '이미지',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', ]