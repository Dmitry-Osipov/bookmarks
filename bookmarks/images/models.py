from django.db import models
from django.conf import settings
from django.utils.text import slugify


# Create your models here.
class Image(models.Model):
    """
    Класс модели формирует таблицу БД со связью к пользователю по ForeignKey, а также имеет поля: заголовок, слаг, url,
    картинка, описание, дата создания и пользователи, которым понравилось изображение.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='images_created')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField(max_length=2000)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='images_liked')

    class Meta:
        """
        Вложенный класс предназначен для корректной обработки данных.
        """
        indexes = [
            models.Index(fields=['-created']),
        ]
        ordering = ['-created']

    def save(self, *args, **kwargs):
        """
        Метод сохраняет экземпляр модели в БД с проверкой слага. Если слаг не заполнен, заполняет его автоматически.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Метод отвечает за более понятный вывод экземпляров класса.

        :return: Информация, к какому логину принадлежит профиль.
        """
        return self.title
