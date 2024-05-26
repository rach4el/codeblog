from django import forms
from .models import ContactUs

#Contact form

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