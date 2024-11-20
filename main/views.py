from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context: [str, str] = {
        "title": "Главная страница",
        "content": "Главная страница магазина - HOME",
    }
    return render(request, "main/index.html", context)


def about(request):
    return HttpResponse("About page")
