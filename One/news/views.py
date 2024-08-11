from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm


# Create your views here.
def home(request):
    news = Post.objects.all().order_by('-pub_date')
    return render(request, 'news/news.html', {'news': news})


@login_required
def create_news(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('news_home')
    else:
        form = PostForm()
    return render(request, 'news/create_news.html', {'form': form})
