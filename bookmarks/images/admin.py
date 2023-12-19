from django.contrib import admin

from .models import Image


# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    """
    Класс служит для обработки модели изображения в админ-панели.
    """
    list_display = ('title', 'slug', 'image', 'created')
    list_filter = ('created', )
