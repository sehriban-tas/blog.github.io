from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render
from pages.models import Post
def index_func(request):
    posts = Post.objects.order_by('published_date')
    return render(request,"home/index.html",{'posts': posts})

def about_func(request):
    return render(request,"page/about.html")

def blog_func(request):
    posts_list = Post.objects.all().order_by('published_date')
    paginator = Paginator(posts_list,2)
    page = request.GET.get('sayfa')
    posts = paginator.get_page(page)
    return render(request,"page/blog.html",{'posts':posts})

def iletisim_func(request):
    return render(request,"page/iletisim.html")

