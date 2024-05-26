from .models import CreatePost
from django import forms


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = CreatePost
        fields = ['title', 'suggested_riding_ability', 'featured_image', 'content', 'excerpt']
        exclude = ['slug', 'approved', 'creator']  
        
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None) 
        super(CreatePostForm, self).__init__(*args, **kwargs)
        self.fields['excerpt'].label = 'Summary:'  

    def save(self, commit=True):
        create_post = super(CreatePostForm, self).save(commit=False)
        if self.request:
            create_post.author = self.request.user
        create_post.slug = self.cleaned_data['title'].lower().replace(' ', '-')  
        create_post.status = 0
        if commit:
            create_post.save()
        return create_post