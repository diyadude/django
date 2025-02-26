from django import forms


class ProfileForm(forms.Form):
    user_image = forms.FileField(
        allow_empty_file=False
    )
    labels = {
        "user_image": "Upload Image",
    }
