from django import forms

from .models import ContactModel


class ContactForm(forms.ModelForm):
    """Contact Form"""
    class Meta:
        model = ContactModel
        exclude = ('create_at',)
        widgets = {
            'name': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'type': 'text', 'placeholder': 'Email'}),
            'website': forms.URLInput(attrs={'type': 'text', 'placeholder': 'Website'}),
            'message': forms.Textarea(attrs={'placeholder': 'Text'}),
        }


