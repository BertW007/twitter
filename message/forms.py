from django import forms
from django.contrib.auth.models import User

from message.models import Message


class MessageCreateForm(forms.ModelForm):
    # content = forms.CharField(widget=forms.Textarea)
    # receiver = forms.CharField(max_length=60)
    #
    # def clean_receiver(self):
    #     receiver = self.cleaned_data['receiver']
    #     if not User.objects.filter(username=receiver):
    #         raise forms.ValidationError('Not found Profile')
    #     return receiver
    class Meta:
        model = Message
        fields = ['content']