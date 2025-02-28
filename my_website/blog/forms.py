from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = [
            'author', 'post'
            ]
        labels = {
            "user_name": "Your name",
            "user_email": "Email address",
            "text": 'Leave your comment'
        }
