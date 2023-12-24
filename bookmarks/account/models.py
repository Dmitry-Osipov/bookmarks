from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Profile(models.Model):
    """
    Класс расширяет стандартную модель пользователя полями с датой рождения и фото по связи один к одному.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        """
        Метод отвечает за более понятный вывод экземпляров класса.

        :return: Информация, к какому логину принадлежит профиль.
        """
        return f'Profile of {self.user.username}'


class Contact(models.Model):
    """
    Класс отвечает за реализацию подписки между пользователями по взаимосвязи многие ко многим с сохранением даты и
    времени подписки.
    """
    user_from = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='rel_from_set')
    user_to = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='rel_to_set')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Вложенный класс предназначен для корректной обработки данных.
        """
        indexes = [
            models.Index(fields=['-created']),
        ]
        ordering = ['-created']

    def __str__(self):
        """
        Метод отвечает за более понятный вывод экземпляров класса.

        :return: Информация, какой пользователь на кого подписался.
        """
        return f'{self.user_from} follows {self.user_to}'


# Добавить следующее поле в User динамически.
user_model = get_user_model()
user_model.add_to_class('following',  # На будущее: данный метод не является рекомендованным.
                        models.ManyToManyField('self',
                                               through=Contact,
                                               symmetrical=False,
                                               related_name='followers'))
