# myapp/views.py
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


def home(request):
    html_content = """
    <h2>Добро пожаловать на мой первый Django-сайт!</h2>
    <p>Это главная страница.</p>
    """

    logger.info('Пользователь посетил главную страницу')

    return render(request, 'home.html', {'html_content': html_content})


def about(request):
    html_content = """
    <h2>О себе</h2>
    <p>Привет! Меня зовут Максим и это моя первая Django-страница.</p>
    """

    logger.info('Пользователь посетил страницу "О себе"')

    return render(request, 'about.html', {'html_content': html_content})
