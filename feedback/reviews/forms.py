from django import forms

from .models import Review


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(
#         max_length=55, label='Name', error_messages={
#             "required": "Your name must not be empty!",
#             "max_length": "Please enter a shorter one"
#         })
#     review_text = forms.CharField(
#         label="Your Feedback", widget=forms.Textarea, max_length=205)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields = "__all__"
        # exclude = []
        fields = [
            'user_name', 'review_text', 'rating'
        ]
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Rate it"
        }
        error_messages = {
            "user_name": {
                "required": "Your name must not be empty!",
                "max_length": "Please enter a shorter one"
            }
        }
