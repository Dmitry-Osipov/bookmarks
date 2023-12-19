from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User

from .models import Profile

class EmailAuthBackend(BaseBackend):
    """
    Бэкенд аутентификации по почте и паролю.
    """
    def authenticate(self, request, username=None, password=None):
        """
        Метод аутентифицирует пользователя по почте и паролю.

        :param request: Запрос клиента.
        :param username: Почта.
        :param password: Пароль.
        :return: Объект пользователя при успешной аутентификации, иначе None.
        """
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None

    def get_user(self, user_id):
        """
        Метод получает пользователя по его pk.

        :param user_id: ID пользователя.
        :return: Объект пользователя при нахождении id в БД, иначе None.
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


def create_profile(backend, user, *args, **kwargs):
    """
    Метод получает или создаёт профиль пользователя для социальной аутентификации.

    :param backend: Используемый для аутентификации пользователей бэкенд социальной аутентификации.
    :param user: Экземпляр класса модели пользователя.
    """
    Profile.objects.get_or_create(user=user)
