from django import forms


class LoginForm(forms.Form):
    """
    Класс формы отвечает за аутентификацию пользователей по БД, используя логин и пароль.
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
