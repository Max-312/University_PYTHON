from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):


    context = {
        'title': 'Easy study - Главная',
        'content': "Учись легко, с Easy study",
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Easy study - О нас',
        'content': "О нас",
        'text_on_page': "Текст о том почему мы такой классный, и крутой сервис."
    }

    return render(request, 'main/about.html', context)