from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(UserLoginForm, self).clean()

        login = cleaned_data['login']
        password = cleaned_data['password']
        self.user = authenticate(username=login, password=password)
        if self.user is None:
            raise forms.ValidationError('Wrong user or password!')
        return cleaned_data


class UserCreateForm(forms.Form):
    username = forms.CharField(max_length=64)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username used!')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email used!')
        return email

    def clean(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if not password1 == password2:
            raise forms.ValidationError('Password wrong!')


class UserEditForm(forms.Form):
    username = forms.CharField(max_length=64)
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    # password1 = forms.CharField(widget=forms.PasswordInput)
    # password2 = forms.CharField(widget=forms.PasswordInput)
    #
    # def clean(self):
    #     password1 = self.cleaned_data['password1']
    #     password2 = self.cleaned_data['password2']
    #     if not password1 == password2:
    #         raise forms.ValidationError('Password wrong!')