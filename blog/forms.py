from .models import Comment, Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'Suggested_Riding_Ability', 'featured_image', 'content', 'excerpt')
        labels = {
            'excerpt': 'Summary:',
            'slug': 'URL',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)