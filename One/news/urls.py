from django.urls import path
from . import views  # импортируем обработчик шаблонов views, чтобы использовать тут в приложении

urlpatterns = [
    path('', views.home, name='news_home'),
]
