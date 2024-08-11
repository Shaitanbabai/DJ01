from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField('Заголовок новости', max_length=50)
    short_description = models.CharField('Краткое описание новости', max_length=200)
    text = models.TextField('Содержание новости')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)  # Автоматически устанавливает время создания
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
