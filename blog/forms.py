from .models import Comment, Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'Suggested_Riding_Ability', 'featured_image', 'content', 'excerpt']
        exclude = ['slug', 'status', 'author']  

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['excerpt'].label = 'Summary:'  

    def save(self, commit=True):
        post = super(PostForm, self).save(commit=False)
        post.author = self.request.user
        post.slug = self.cleaned_data['title'].lower().replace(' ', '-')  
        post.status = 0
        if commit:
            post.save()
        return post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)