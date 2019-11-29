
from django.contrib import admin
from django.urls import path
from pages.views import index_func,about_func,blog_func,iletisim_func

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index_func),

    path("home/index",index_func),
    path("page/about",about_func),
    path("page/blog",blog_func),
    path("page/iletisim",iletisim_func)

]
