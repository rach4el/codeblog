from django import forms
from .models import ContactUs

# Model for contact us form


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['query_title', 'query_image', 'content']

    def clean(self):
        cleaned_data = super().clean()
        query_title = cleaned_data.get('query_title')
        content = cleaned_data.get('content')
        if not query_title or not content:
            raise forms.ValidationError('Please fill in all fields')
        return cleaned_data

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ContactUsForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(ContactUsForm, self).save(commit=False)
        if self.user:
            instance.author = self.user
        if commit:
            instance.save()
        return instance