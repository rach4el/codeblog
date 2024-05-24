from .models import CreatePost
from django import forms


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = CreatePost
        fields = ['title', 'suggested_riding_ability', 'featured_image', 'content', 'excerpt']