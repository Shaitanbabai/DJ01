from django.urls import path
from . import views  # импортируем обработчик шаблонов views, чтобы использовать тут в приложении

urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.new, name='new'),
    path('data', views.data, name='data'),
    path('test', views.test, name='test'),
]
