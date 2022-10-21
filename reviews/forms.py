from django import forms
from django import forms
from .models import Review, Comment
from django.forms import ModelForm, TextInput, Textarea

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        widget = {
            'title' : forms.TextInput(
                attrs={
                    'placeholder' : '제목을 입력해주세요.'
                }
            ),
            'content' : forms.Textarea(
                attrs={
                    'placeholder' : '내용을 입력해주세요.'
                }
            )
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', ]