from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .validators import validate_password
from .models import Client, MyUser
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate


class UserAddForm(forms.ModelForm):
    password_2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        ]
        widgets = {
            'password': forms.PasswordInput,
        }

    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['password_2']:
            raise forms.ValidationError('Password aren"t same')
        else:
            self.cleaned_data.pop('password_2')
        return self.cleaned_data

    def clean_username(self):
        username = self.cleaned_data['username']
        user = get_user_model()
        if len(user.objects.filter(username=username)) != 0:
            raise forms.ValidationError('User already exists')
        return username


class LoginForm(forms.Form):
    login = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput)



class UserResetPasswordForm(forms.Form):
    new_password_1 = forms.CharField(widget=forms.PasswordInput, label='New password')
    new_password_2 = forms.CharField(widget=forms.PasswordInput, label='Repeat password')

    def clean(self):
        if self.cleaned_data['new_password_1'] != self.cleaned_data['new_password_2']:
            raise forms.ValidationError('Passwords arent same')
        return self.cleaned_data

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'
