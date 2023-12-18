from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .forms import *
from .models import Profile


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


def register(request):
    """
    Функция представления выводит форму регистрации.

    :param request: Запрос клиента.
    :return: HTML-шаблон регистрации пользователя.
    """
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', context={'new_user': new_user})
    else:
        user_form = UserRegistrationForm()

    return render(request, 'account/register.html', context={'user_form': user_form})


@login_required
def edit(request):
    """
    Функция представления выводит форму изменения профиля.

    :param request: Запрос клиента.
    :return: HTML-страница изменения профиля.
    """
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'account/edit.html',
                  context={'user_form': user_form, 'profile_form': profile_form})
