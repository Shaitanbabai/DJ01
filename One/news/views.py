from django.shortcuts import render
from .models import Post


# Create your views here.
def home(request):
    news = Post.objects.all()
    return render(request, 'news/news.html', {'news': news})
