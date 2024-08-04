from django.shortcuts import render
from django.http import HttpResponse


# файл для отображения HTML-шаблонов. При получении URL-адреса произойдет переход на какую-либо HTML-страницу
def index(request):
    # return HttpResponse("<h1>Это мой первый проект на Django</h1>")
    return render(request, 'main/index.html')


def new(request):
    # return HttpResponse("<h1>Это еще одна страница проекта на Django</h1>")
    return render(request, 'main/new.html')


def data(request):
    # return HttpResponse("<h1>Страница №3 для домашки DJ02 </h1>")
    return render(request, 'main/data.html')


def test(request):
    # return HttpResponse("<h1>Cтраница №4 для домашки DJ02 </h1>")
    return render(request, 'main/test.html')
