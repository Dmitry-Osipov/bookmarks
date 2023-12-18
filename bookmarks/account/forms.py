from django import forms
from django.contrib.auth.models import User

from .models import Profile


class LoginForm(forms.Form):
    """
    Класс формы отвечает за аутентификацию пользователей по БД, используя логин и пароль.
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    """
    Класс формы отвечает за регистрацию пользователей.
    """
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Repeat password')

    class Meta:
        """
        Вложенный класс предназначен для корректной обработки данных.
        """
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        """
        Метод проводит проверку введённых паролей.

        :return: Пароль.
        :raises ValidationError: Пароли не совпадают.
        """
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    """
    Класс позволяет редактировать своё имя, фамилию и адрес электронной почты, которые являются атрибутами модели User.
    """
    class Meta:
        """
        Вложенный класс предназначен для корректной обработки данных.
        """
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    """
    Класс позволяет редактировать дату рождения и фото, которые являются атрибутами модели Profile.
    """
    class Meta:
        """
        Вложенный класс предназначен для корректной обработки данных.
        """
        model = Profile
        fields = ('date_of_birth', 'photo')
