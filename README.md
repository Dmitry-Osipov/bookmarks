# Приложение социального веб-сайта с использованием Python 3.11 и Django 4.1.13
## Описание и технологии проекта
- Социальный веб-сайт.
- Реализована аутентификация пользователей по логину и паролю.
- Реализована возможность смены пароля через почту.
- Стандартная модель пользователя расширена новой моделью со связью один к одному.
## Структура папок
bookmarks - sources root:
- account - пакет приложения аутентификации:
    - migrations - пакет служит для хранения миграций БД;
    - static - папка статики:
        - css - папка стилей. 
    - templates - папка шаблонов:
        - account - папка служит для избежания коллизий:
            - dashboard.html - шаблон профиля пользователя; 
            - edit.html - шаблон изменения профиля пользователя;
            - login.html - шаблон кастомной аутентификации;
            - register.html - шаблон регистрации;
            - register_done.html - шаблон успешного прохождения регистрации.
        - registration - папка стандартной аутентификации:
            - logged_out.html - шаблон выхода из сайта; 
            - login.html - шаблон стандартной аутентификации;
            - password_change_done.html - шаблон успешной смены пароля;
            - password_change_form.html - шаблон смены пароля.
            - password_reset_complete.html - шаблон успешного восстановления пароля;
            - password_reset_confirm.html - шаблон подтверждения сброса пароля;
            - password_reset_done.html - шаблон инструкций по сбросу пароля;
            - password_reset_email.html - шаблон сообщения в письме по сбросу пароля;
            - password_reset_form.html - шаблон сброса пароля.
        - base.html - базовый шаблон.
    - __init__.py - файл указывает питону, что данная директория является пакетом;
    - admin.py – файл для настройки админ-панели сайта (админ-панель поставляется совместно с Django и каждый сайт может сразу ее использовать);
    - apps.py – файл для настройки (конфигурирования) текущего приложения;
    - forms.py - файл для хранения форм;
    - models.py – файл для хранения ORM-моделей для представления данных из базы данных;
    - tests.py – модуль с тестирующими процедурами;
    - urls.py - файл для хранения всех перенаправлений клиента;
    - views.py – файл для хранения представлений (контроллеров) текущего приложения.
- bookmarks - пакет конфигурации:
    - __init__.py - файл указывает питону, что данная директория является пакетом;
    - asgi.py - это точка входа для веб-серверов, которые поддерживают ASGI (Asynchronous Server Gateway Interface);
    - settings.py - файл настроек сайта;
    - urls.py - файл для хранения всех перенаправлений клиента;
    - wsgi.py -  это точка входа для веб-серверов, которые поддерживают WSGI (Web Server Gateway Interface).
- media - папка фото профилей пользователей, сохранение идёт по иерархии года, месяца и дня; 
- db.sqlite3 - база данных сайта;
- manage.py - файл, который передаёт команды django-admin и выполняет их "от лица" сайта.