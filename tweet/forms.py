from django import forms

from tweet.models import Tweet


class UserTweetCreateForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']