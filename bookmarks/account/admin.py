from django.contrib import admin
from .models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Класс служит для обработки модели профиля в админ-панели.
    """
    list_display = ('user', 'date_of_birth', 'photo')
    raw_id_fields = ('user', )
