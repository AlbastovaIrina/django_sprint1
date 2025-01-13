from django.apps import AppConfig


class PagesConfig(AppConfig):
    """
    Этот класс определяет конфигурацию приложения 'pages'.
    Он наследуется от AppConfig и используется Django для управления
    настройками приложения.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'
