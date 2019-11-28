from django.shortcuts import render

def index_func(request):
    return render(request,"home/index.html")
