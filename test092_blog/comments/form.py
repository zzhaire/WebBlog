from django import forms


class CommentForm(forms.Form):
    content = forms.CharField(min_length=1, max_length=300)
