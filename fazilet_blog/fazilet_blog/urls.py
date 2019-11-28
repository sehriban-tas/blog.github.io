
from django.contrib import admin
from django.urls import path
from pages.views import index_func

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index_func)
]
