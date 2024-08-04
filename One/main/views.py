from django.shortcuts import render
from django.http import HttpResponse


# файл для отображения HTML-шаблонов. При получении URL-адреса произойдет переход на какую-либо HTML-страницу
def index(request):
    return HttpResponse("<h1>Это мой первый проект на Django</h1>")


def new(request):
    return HttpResponse("<h1>Это еще одна страница проекта на Django</h1>")


def data(request):
    return HttpResponse("<h1>Страница №1 для домашки </h1>")


def test(request):
    return HttpResponse("<h1>траница №2 для домашки </h1>")
