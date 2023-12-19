from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404

from .forms import ImageCreateForm
from .models import Image


# Create your views here.
@login_required
def image_create(request):
    """
    Функция представления отвечает за формирование шаблона хранения изображения на сайте.

    :param request: Запрос клиента.
    :return: HTML-шаблон хранения изображения.
    """
    if request.method == 'POST':
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            new_image = form.save(commit=False)
            new_image.user = request.user  # Передача текущего пользователя пользователю элемента.
            new_image.save()
            messages.success(request, 'Image added successfully')
            return redirect(new_image.get_absolute_url())
    else:
        form = ImageCreateForm(data=request.GET)

    return render(request, 'images/image/create.html', context={'section': 'images', 'form': form})


def image_detail(request, id, slug):
    """
    Функция представления отвечает за вывод изображения на страницу.

    :param request: Запрос клиента.
    :param id: ID изображения.
    :param slug: Слаг изображения.
    :return: HTML-шаблон отображения изображения.
    """
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request, 'images/image/detail.html', context={'section': 'images', 'image': image})
