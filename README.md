# Приложение социального веб-сайта с использованием Python 3.11 и Django 4.1.13
## Описание и технологии проекта
- Социальный веб-сайт.
## Структура папок
bookmarks - sources root:
- account - пакет приложения аутентификации:
    - migrations - пакет служит для хранения миграций БД;
    - static - папка статики:
        - css - папка стилей. 
    - templates - папка шаблонов:
        - account - папка служит для избежания коллизий:
            - login.html - шаблон аутентификации. 
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
- db.sqlite3 - база данных сайта;
- manage.py - файл, который передаёт команды django-admin и выполняет их "от лица" сайта.