from django.db import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.




class RegisterForm(forms.Form):
    login = forms.CharField(label='Login', min_length=5)
    password = forms.CharField(label='Password', min_length=8, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password', min_length=8, widget=forms.PasswordInput)
    email = forms.CharField(label='Email', min_length=1)
    surname = forms.CharField(label='Surname', min_length=1)
    name = forms.CharField(label='Name', min_length=1)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Пароли не совпадают")
        usrs = User.objects.filter(username=cleaned_data.get('login'))
        if len(usrs) > 0:
            raise forms.ValidationError("Пользователь с данным логином уже существует")


class LoginForm(forms.Form):
    login = forms.CharField(label='Login', min_length=5)
    password = forms.CharField(label='Password', min_length=8, widget=forms.PasswordInput)

class Book_User(models.Model):
	user=models.CharField(max_length=200)
	book=models.CharField(max_length=100)
	number=models.IntegerField()