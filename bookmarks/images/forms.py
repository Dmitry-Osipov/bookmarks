import requests
from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify

from .models import Image


class ImageCreateForm(forms.ModelForm):
    """
    Класс формы предназначен за добавление изображения.
    """
    class Meta:
        """
        Вложенный класс предназначен для корректной обработки данных.
        """
        model = Image
        fields = ('title', 'url', 'description')
        widgets = {
            'url': forms.HiddenInput,
        }

    def clean_url(self):
        """
        Метод проверяет расширение изображения на принадлежность JPEG или PNG.

        :return: URL.
        :raises: ValidationError: Указано неверное расширение изображения.
        """
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('The given URL does not match valid image extensions.')
        return url

    def save(self, force_insert=False, force_update=False, commit=True):
        """
        Метод позволяет сохранять данные в БД.

        :return:
        """
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'{name}.{extension}'
        response = requests.get(image_url)  # Скачиваем изображение по URL.
        image.image.save(image_name, ContentFile(response.content), save=False)

        if commit:
            image.save()

        return image

