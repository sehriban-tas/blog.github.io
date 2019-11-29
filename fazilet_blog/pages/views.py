from django.shortcuts import render
from pages.models import Post
def index_func(request):
    posts = Post.objects.order_by('published_date')
    return render(request,"home/index.html",{'posts': posts})

def about_func(request):
    return render(request,"page/about.html")

def blog_func(request):
    return render(request,"page/blog.html")

def iletisim_func(request):
    return render(request,"page/iletisim.html")