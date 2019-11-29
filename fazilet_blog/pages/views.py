from django.shortcuts import render

def index_func(request):
    return render(request,"home/index.html")

def about_func(request):
    return render(request,"page/about.html")

def blog_func(request):
    return render(request,"page/blog.html")

def iletisim_func(request):
    return render(request,"page/iletisim.html")