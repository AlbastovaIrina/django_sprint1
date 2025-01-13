from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Этот класс определяет конфигурацию приложения 'blog'.
    Он наследуется от AppConfig и используется Django для управления
    настройками приложения.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
