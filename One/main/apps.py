from django.apps import AppConfig  # файл с настройками, но не общими, а для конкретного приложения main


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
