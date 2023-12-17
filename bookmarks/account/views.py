from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import LoginForm

# Create your views here.
def user_login(request):
    """
    Функция представления отвечает за формирование страницы входа.

    :param request: Запрос клиента.
    :return: HTML-страница аутентификации.
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                return HttpResponse('Disabled account')
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()

    return render(request, 'account/login.html', context={'form': form})


@login_required
def dashboard(request):
    """
    Функция представления показывает аутентифицированным пользователям информационную панель.

    :param request: Запрос клиента.
    :return: HTML-шаблон информационной панели.
    """
    return render(request, 'account/dashboard.html', context={'section': 'dashboard'})
