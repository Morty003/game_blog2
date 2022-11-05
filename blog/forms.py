from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post', 'create_at']
        widgets = {
            'name': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'type': 'text', 'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Text'}),
        }