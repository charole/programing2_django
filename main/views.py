from django.shortcuts import render
from .models import Post

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def blog(request):
    postlist = Post.objects.all()
    # dictionary single quote 없으면 데이터 안넘어감
    return render(request, 'main/blog.html', {'postlist': postlist})
