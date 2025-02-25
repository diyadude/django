from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(
        max_length=55, label='Name', error_messages={
            "required": "Your name must not be empty!",
            "max_length": "Please enter a shorter one"
        })
    review_text = forms.CharField(
        label="Your Feedback", widget=forms.Textarea, max_length=205)
    rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)
