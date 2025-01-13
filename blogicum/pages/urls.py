"""URL-паттерны для приложения pages."""
from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    # URL-паттерн для страницы "О нас"
    path('about/', views.about, name='about'),
    
    # URL-паттерн для страницы правил
    path('rules/', views.rules, name='rules'),
]
