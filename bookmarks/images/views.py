from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

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


@login_required
@require_POST
def image_like(request):
    """
    Функция представления отвечает за отображение лайков и дизлайков для изображения.

    :param request: Запрос клиента.
    :return: Ответ в формате json.
    """
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except Image.DoesNotExist:
            pass
    return JsonResponse({'status': 'error'})


@login_required
def image_list(request):
    """
    Функция представления отвечает за бесконечную постраничную прокрутку.

    :param request: Запрос клиента.
    :return: HTML-шаблон представления всех изображений.
    """
    images = Image.objects.all()
    paginator = Paginator(images, 8)
    page = request.GET.get('page')
    images_only = request.GET.get('images_only')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        if images_only:
            return HttpResponse('')
        images = paginator.page(paginator.num_pages)

    if images_only:
        return render(request, 'images/image/list_images.html',
                      context={'section': 'images', 'images': images})
    return render(request, 'images/image/list.html', context={'section': 'images', 'images': images})
