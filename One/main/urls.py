from django.urls import path
from . import views  # импортируем обработчик шаблонов views, чтобы использовать тут в приложении

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('data', views.new),
    path('test', views.new),
]
