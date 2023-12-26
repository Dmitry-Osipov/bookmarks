from django.db import models

# Create your models here.
class Action(models.Model):
    """
    Класс модели используется для хранения действий пользователя. Модель хранит пользователя, его действие, дату и время
    самого действия.
    """
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='actions')
    verb = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Вложенный класс предназначен для корректной обработки данных.
        """
        indexes = [
            models.Index(fields=['-created']),
        ]
        ordering = ['-created']
