"""
URL-паттерны для приложения.

Этот список содержит URL-паттерны,
которые определяют маршруты для страницвеб-приложения.

Каждый паттерн связан с соответствующей функцией представления
и получает уникальное имя для удобства ссылок и редиректов.
"""

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path(
        'category/<slug:category_slug>/',
        views.category_posts,
        name='category_posts')
]
